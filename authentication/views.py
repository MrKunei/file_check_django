from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import CustomUserCreationForm


class SignupView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('core:files_list_view')
    success_message = 'Account created successfully!'


class SigninView(LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/signin.html'


class SignoutView(SuccessMessageMixin, LogoutView):
    success_message = 'You are logged out!'