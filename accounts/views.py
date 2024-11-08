from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

def home_view(request):
    return render(request, 'home.html')  # Renderiza la plantilla home.html

def plantilla_view(request):
    return render(request, 'plantilla.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirige a login tras el registro
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Usa tu plantilla personalizada para login

class CustomLogoutView(LogoutView):
    template_name = 'registration/out.html'  # Usa tu plantilla personalizada para logout
