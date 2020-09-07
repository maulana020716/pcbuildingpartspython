from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import UserCreateForm
from accounts.models import User

from . import forms

class SignUp(SuccessMessageMixin, CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
    success_message = "Terimakasih telah mendaftar, Silahkan login dengan akun anda !"




class UserUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    template_name = "accounts/profile.html"
    redirect_field_name = 'accounts/profile.html'
    form_class = UserCreateForm
    model = User
