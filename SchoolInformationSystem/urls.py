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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', sign_up, name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('my_profile/', my_profile, name='my_profile')
]
