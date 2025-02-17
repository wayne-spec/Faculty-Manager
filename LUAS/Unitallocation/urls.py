from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import auth_status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import auth_status


urlpatterns = [
    # Academic Year URLs
    path('academicyears/', views.AcademicYearListCreateView.as_view(), name='academic-year-list-create'),
    path('academicyears/<int:pk>/', views.AcademicYearRetrieveUpdateView.as_view(), name='academic-year-retrieve-update'),
    

    # Course URLs
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseUpdateRetrieveView.as_view(), name='course-retrieve-update'),
    
    # Semester URLs
    path('semesters/', views.SemesterListCreateView.as_view(), name='semester-list-create'),
    path('semesters/<int:pk>/', views.SemesterRetrieveUpdateView.as_view(), name='semester-retrieve-update'),
    
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/',views.UserDetailAPIView.as_view(), name='user-detail'),

    # School URLs
    path('schools/', views.SchoolsListCreateView.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', views.SchoolRetrieveUpdateView.as_view(), name='school-retrieve-update'),
    
    # Unit Type URLs
    path('unittypes/', views.UnitTypeListCreateView.as_view(), name='unit-type-list-create'),
    path('unittypes/<int:pk>/', views.UnitTypeRetrieveUpdateView.as_view(), name='unit-type-retrieve-update'),
    
    # Unit URLs
    path('units/', views.UnitListCreateView.as_view(), name='unit-list-create'),
    path('units/<int:pk>/', views.UnitRetrieveUpdateView.as_view(), name='unit-retrieve-update'),
    
    # Faculty Field URLs
    path('fields/', views.FieldListCreateView.as_view(), name='field-list-create'),
    path('fields/<int:pk>/', views.FieldRetrieveUpdateView.as_view(), name='field-retrieve-update'),
    
    # Faculty URLs
    path('faculties/', views.FacultyListCreateView.as_view(), name='faculty-list-create'),
    path('faculties/<int:pk>/', views.FacultyRetrieveUpdateView.as_view(), name='faculty-retrieve-update'),
    
    # Faculty Type URLs
    path('facultytypes/', views.FacultyTypeListCreateView.as_view(), name='faculty-type-list-create'),
    path('facultytypes/<int:pk>/', views.FacultyTypeRetrieveUpdateView.as_view(), name='faculty-type-retrieve-update'),
    
    # Unit Allocation URLs
    path('unitallocations/', views.UnitAllocationListCreateView.as_view(), name='unit-allocation-list-create'),
    path('unitallocations/<int:pk>/', views.UnitAllocationRetrieveUpdateView.as_view(), name='unit-allocation-retrieve-update'),
    
    # Max Allocations URLs
    path('maxallocations/', views.MaxAllocationsListCreateView.as_view(), name='max-allocations-list-create'),
    path('maxallocations/<int:pk>/', views.MaxAllocationsRetrieveUpdateView.as_view(), name='max-allocations-retrieve-update'),
    
    # Login View URL



    path("api/user/register/", views.createUserView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("api-auth/", include("rest_framework.urls")),
    


    path('login/',views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),

    path('auth-status/', auth_status, name='auth_status'),
]
