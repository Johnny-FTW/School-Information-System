from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

from .models import *


class StudentSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email')
        user.is_student = True
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        student = Student.objects.create(user=user, first_name=first_name, last_name=last_name )
        student.save()

        return user


class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email')
        user.is_teacher = True
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        teacher = Teacher.objects.create(user=user, first_name=first_name, last_name=last_name )
        teacher.save()

        return user