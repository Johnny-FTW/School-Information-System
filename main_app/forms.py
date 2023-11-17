from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import forms

from .models import *


class StudentSignupForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    email = forms.Field(required=True)

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
