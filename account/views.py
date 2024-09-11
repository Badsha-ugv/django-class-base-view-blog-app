from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth.views import LoginView


from .forms import UserCreationForm

class RegisterUser(generic.FormView):
    form_class = UserCreationForm 
    template_name = 'account/register.html'
    success_url = reverse_lazy('blog:blog-list')


class UserLogin(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('blog:blog-list')

    def get_success_url(self):
        return self.success_url

