from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.generic import ListView, TemplateView
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.
def login_user(request):
    context = {'login_form': LoginForm()}
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            context = {
                'login_form': login_form
            }
    return render(request, 'account/login.html', context)

class RegisterView(TemplateView):
    template_name = 'account/register.html'
    
    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'account/register.html', context)
    
    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            
            return redirect('home')
        
        context = {'user_form': user_form}
        return render(request, 'account/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')