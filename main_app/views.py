from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from main_app.forms import SignUpForm


def home(request):
    return render(request, 'home.html')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'