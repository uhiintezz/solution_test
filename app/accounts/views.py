from django.contrib.auth import login, logout
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . forms import *

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'


    def get_success_url(self):
        return reverse_lazy('home')


    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)

        return super().form_valid(form)



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        user = form.save()

        login(self.request, user)

        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')