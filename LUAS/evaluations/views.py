from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, authenticate
from .serializers import EvaluationQuestionSerializer, EvaluationSerializer, EvaluationResponseSerializer
from .models import EvaluationQuestion, Evaluation, EvaluationResponse
from django.contrib.auth import login, logout
# Custom permission
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

# Evaluation Question Views
class EvaluationQuestionView(generics.ListCreateAPIView):
    queryset = EvaluationQuestion.objects.all()
    serializer_class = EvaluationQuestionSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class EvaluationQuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EvaluationQuestion.objects.all()
    serializer_class = EvaluationQuestionSerializer
    permission_classes = [AllowAny]

# Evaluation Views
class EvaluationView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.prefetch_related('questions').all()
    serializer_class = EvaluationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class EvaluationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.prefetch_related('questions').all()
    serializer_class = EvaluationSerializer
    permission_classes = [AllowAny]

# Evaluation Response Views
from django.utils.timezone import now

class EvaluationResponseView(generics.ListCreateAPIView):
    queryset = EvaluationResponse.objects.all()
    serializer_class = EvaluationResponseSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Request data is now a list of responses
        responses_data = request.data
        
        if not responses_data:
            return Response(
                {"error": "No responses provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Get evaluation_id from the first response
            evaluation_id = responses_data[0].get('evaluation_id')
            evaluation = Evaluation.objects.get(id=evaluation_id)
        except (KeyError, IndexError):
            return Response(
                {"error": "Missing evaluation_id in payload"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Evaluation.DoesNotExist:
            return Response(
                {"error": "Evaluation not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Validate all responses belong to the same evaluation
        for response in responses_data:
            if response.get('evaluation_id') != evaluation_id:
                return Response(
                    {"error": "All responses must belong to the same evaluation"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Get evaluation questions
        question_ids = set(evaluation.questions.values_list('id', flat=True))
        
        # Validate responses
        response_question_ids = {r['question_id'] for r in responses_data}
        
        if response_question_ids != question_ids:
            return Response(
                {"error": "Response questions don't match evaluation questions"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create responses
        serializer = self.get_serializer(data=responses_data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {"message": "Evaluation submitted successfully"},
            status=status.HTTP_201_CREATED
        )


class EvaluationResponseRetrieveView(generics.RetrieveAPIView):
    queryset = EvaluationResponse.objects.select_related('evaluation', 'question').all()
    serializer_class = EvaluationResponseSerializer
    permission_classes = [AllowAny]

# CSRF Exempt Authentication
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # Disable CSRF check
        return

# Login View
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

# Logout View
@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

# Auth Status View
def auth_status(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({"isAuthenticated": is_authenticated})
