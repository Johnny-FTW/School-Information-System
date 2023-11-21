from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import CreateView

from main_app.forms import StudentSignupForm, TeacherSignUpForm
from main_app.models import User


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    return render(request, 'register.html')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

