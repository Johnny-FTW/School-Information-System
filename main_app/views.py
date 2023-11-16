from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    return render(request, 'home.html')

