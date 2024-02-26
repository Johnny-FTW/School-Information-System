from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from main_app.forms import StudentSignupForm, TeacherSignUpForm, StudentForm, TeacherForm, ExamForm
from main_app.models import User, Student, Teacher, Exam, Subject, Classroom, SubjectSchedule


def home(request):
    return render(request, 'home.html')


@permission_required('main_app.add_user')
def register_users(request):
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
    template_name = 'register_users.html'
    permission_required = ['main_app.add_user', 'main_app.add_student']

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('register_users')


class TeacherSignUpView(PermissionRequiredMixin, CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'register_users.html'
    permission_required = ['main_app.add_user', 'main_app.add_teacher']

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            user = form.save()
            teacher_group = Group.objects.get(name='teacher')
            user.groups.add(teacher_group)
            return redirect('register_users')
        except Exception:
            return HttpResponse("Error: The 'teacher' group does not exist.", status=500)


@login_required
def my_profile(request):
    user = User.objects.get(pk=request.user.pk)
    context = {'user': user}
    return render(request, 'my_profile.html', context)


@login_required
def profile(request, pk):
    user = User.objects.get(id=pk)
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


class ExamCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'new_exam.html'
    form_class = ExamForm
    permission_required = 'main_app.add_exam'

    def form_valid(self, form):
        student_id = self.kwargs['student_id']
        subject_id = self.kwargs['subject_id']
        subject = Subject.objects.get(id=subject_id)
        student = Student.objects.get(user_id=student_id)
        form.instance.subject = subject
        form.instance.student = student
        return super().form_valid(form)

    def get_success_url(self):
        subject_id = self.kwargs['subject_id']
        return reverse_lazy('subject_detail', kwargs={'pk': subject_id})


class ExamUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'new_exam.html'
    model = Exam
    form_class = ExamForm
    permission_required = 'main_app.change_exam'

    def get_success_url(self):
        exam = self.get_object()
        subject_id = exam.subject_id
        return reverse_lazy('subject_detail', kwargs={'pk': subject_id})


class ExamDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'exam_confirm_delete.html'
    model = Exam
    permission_required = 'main_app.delete_exam'

    def get_success_url(self):
        exam = self.get_object()
        subject_id = exam.subject_id
        return reverse_lazy('subject_detail', kwargs={'pk': subject_id})


@login_required
def exam_detail(request, pk):
    exam = Exam.objects.get(id=pk)
    teacher = exam.subject.teacher
    context = {'exam': exam, 'teacher': teacher}
    return render(request, 'exam_detail.html', context)


@login_required
def my_subjects(request):
    if request.user.is_student:
        my_subjects = Subject.objects.filter(student=request.user.student)
    elif request.user.is_teacher:
        my_subjects = Subject.objects.filter(teacher=request.user.teacher)
    else:
        my_subjects=None
    context = {'my_subjects': my_subjects}
    return render(request, 'my_subjects.html', context)


@login_required
def subject_detail(request, pk):
    subject = Subject.objects.get(id=pk)
    exams = Exam.objects.filter(subject=subject)
    schedules = SubjectSchedule.objects.filter(subject=subject)
    context = {'subject': subject, 'exams': exams, 'schedules': schedules}
    return render(request, 'subject_detail.html', context)


@login_required
def classroom_detail(request, pk):
    classroom = Classroom.objects.get(id=pk)
    context = {'classroom': classroom}
    return render(request, 'classroom_detail.html', context)

