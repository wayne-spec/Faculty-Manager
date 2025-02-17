from django.shortcuts import render
from rest_framework import generics,viewsets,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import (AcademicYear, School, Course, Semester, UnitType, Unit, Field, Faculty, FacultyType, UnitAllocation, MaxAllocations)
from .serializers import (UserSerializer,AcademicYearSerializer, SchoolSerializer, CourseSerializer, SemesterSerializer, UnitTypeSerializer, UnitSerializer, FieldSerializer, FacultySerializer, FacultyTypeSerializer, UnitAllocationSerializer, MaxAllocationsSerializer)
from django.utils.timezone import now
from rest_framework import permissions
from django.http import JsonResponse
from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import GroupSerializer
# Create your views here.
class createUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    
    
# imports remain unchanged

class AcademicYearListCreateView(generics.ListCreateAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AcademicYearRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CourseUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class SemesterListCreateView(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SemesterRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class SchoolsListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class SchoolRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class UnitTypeListCreateView(generics.ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class UnitTypeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class UnitListCreateView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        if not course_id:
            raise serializers.ValidationError({"course": "This field is required."})
        course = Course.objects.get(id=course_id)
        serializer.save(course=course, school=course.school)


class UnitRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        course_id = self.request.data.get('course')
        if not course_id:
            raise serializers.ValidationError({"course": "This field is required."})
        course = Course.objects.get(id=course_id)
        serializer.save(course=course, school=course.school)


class FieldListCreateView(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class FieldRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve, update, or delete a specific user
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FacultyListCreateView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get school filter from query params
        school = self.request.query_params.get('school', None)
        
        if school:
            queryset = queryset.filter(school__id=school)  # Filter by school id
        
        return queryset    


class FacultyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Faculty.objects.all().order_by('last_name', 'first_name')
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class FacultyTypeListCreateView(generics.ListCreateAPIView):
    queryset = FacultyType.objects.all()
    serializer_class = FacultyTypeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class FacultyTypeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = FacultyType.objects.all()
    serializer_class = FacultyTypeSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class UnitAllocationListCreateView(generics.ListCreateAPIView):
    queryset = UnitAllocation.objects.all()
    serializer_class = UnitAllocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UnitAllocationRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UnitAllocation.objects.all()
    serializer_class = UnitAllocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)


class MaxAllocationsListCreateView(generics.ListCreateAPIView):
    queryset = MaxAllocations.objects.all()
    serializer_class = MaxAllocationsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class MaxAllocationsRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaxAllocations.objects.all()
    serializer_class = MaxAllocationsSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # Disable CSRF check
        return
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
                login(request, user)  # Log the user in
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)  # Log the user out
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

def auth_status(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({"isAuthenticated": is_authenticated})    
    