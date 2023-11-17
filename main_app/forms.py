from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

from .models import *


class StudentSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    destination = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'destination', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email')  # You may customize the username as per your requirements
        user.is_teacher = True
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        teacher = Teacher.objects.create(user=user)
        teacher.phone = self.cleaned_data.get('phone')
        teacher.destination = self.cleaned_data.get('destination')
        teacher.save()

        return user