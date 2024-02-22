"""
URL configuration for SchoolInformationSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register_users/', register_users, name='register_users'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('my_profile/', my_profile, name='my_profile'),
    path('my_profile/update/student', ProfileUpdateViewStudent.as_view(), name='edit_profile_student'),
    path('my_profile/update/teacher', ProfileUpdateViewTeacher.as_view(), name='edit_profile_teacher'),
    path('add_exam/<int:subject_id>/<int:student_id>/', ExamCreateView.as_view(), name='add_exam'),
    path('update_exam/<pk>/', ExamUpdateView.as_view(), name='update_exam'),
    path('delete_exam/<pk>/', ExamDeleteView.as_view(), name='delete_exam'),
    path('exam_detail/<pk>/', exam_detail, name='exam_detail'),
    path('my_subjects/', my_subjects, name='my_subjects'),
    path('subject_detail/<pk>/', subject_detail, name='subject_detail'),
]
