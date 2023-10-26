from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    return render(request, 'home.html')

