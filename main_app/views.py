from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from main_app.forms import StudentSignupForm, TeacherSignUpForm, StudentForm, TeacherForm
from main_app.models import User, Student, Teacher


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    return render(request, 'register.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        print(f"request.user: {request.user}")
        if request.user.is_authenticated:
            print("User is authenticated. Redirecting to 'home'")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        next_page = super().get_next_page()
        if next_page:
            return next_page
        else:
            return 'home'


class StudentSignUpView(PermissionRequiredMixin, CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'signup.html'
    permission_required = 'main_app.can_sign_up_student'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class TeacherSignUpView(PermissionRequiredMixin, CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup.html'
    permission_required = 'main_app.sign_up'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


@login_required
def my_profile(request):
    user = User.objects.get(pk=request.user.pk)
    context = {'user': user}
    return render(request, 'my_profile.html', context)


class ProfileUpdateViewStudent(UpdateView):
    template_name = 'edit_profile.html'
    model = Student
    form_class = StudentForm

    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, pk=self.request.user.student.pk)
        return obj

    def get_success_url(self):
        return reverse_lazy('my_profile')


class ProfileUpdateViewTeacher(UpdateView):
    template_name = 'edit_profile.html'
    model = Teacher
    form_class = TeacherForm

    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, pk=self.request.user.teacher.pk)
        return obj

    def get_success_url(self):
        return reverse_lazy('my_profile')

