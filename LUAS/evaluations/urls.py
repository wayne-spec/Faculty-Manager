from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import auth_status

app_name = 'evaluations'

urlpatterns = [
    # Evaluation URLs
    path('evaluations/', views.EvaluationView.as_view(), name='create-evaluation'),
    path('evaluations/<int:pk>/', views.EvaluationDetailView.as_view(), name='retrieve-update-evaluation'),
    
    # Evaluation Question URLs
    path('evaluationquestions/', views.EvaluationQuestionView.as_view(), name='create-evaluation-question'),
    path('evaluationquestions/<int:pk>/', views.EvaluationQuestionDetailView.as_view(), name='evaluation-question-retrieve-update'),
    
    # Evaluation Response URLs
    path('evaluationresponses/', views.EvaluationResponseView.as_view(), name='evaluation-response-list-create'),
    path('evaluationresponses/<int:pk>/', views.EvaluationResponseRetrieveView.as_view(), name='evaluation-response-retrieve-update'),

    
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # DRF Authentication
    path("api-auth/", include("rest_framework.urls")),
    
    # Login and Logout
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Auth Status
    path('auth-status/', auth_status, name='auth_status'),
]
