from http.client import HTTPResponse
from urllib import request
from django.views.generic import ListView, TemplateView
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, logout, login

from .forms import *
from .models import *

class EventHome(ListView):
    model = Event
    template_name = 'tickets/home.html'
    context_object_name = 'events'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ticketee — продажа билетов'
        context['cat_selected'] = ""
        
        return context
    
def events(request):
    return render(request, 'tickets/events.html', {'title': 'События | Ticketee'})

def about(request):
    return render(request, 'tickets/about.html', {'title': 'О нас | Ticketee'})

def show_event(request, event_slug, cat_slug):
    event = get_object_or_404(Event, slug=event_slug)
    
    return render(request, 'tickets/event.html', {'event': event, 'title': event.name, 'cat_selected': cat_slug})

def show_events_by_category(request, cat_slug):
    category = get_object_or_404(Category, slug = cat_slug)
    context = {
        'title' : f'{category.name} | Ticketee',
        'cat_selected' : cat_slug,
    }
    
    return render(request, 'tickets/events_by_category.html', context=context)


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
    return render(request, 'tickets/login.html', context)

class RegisterView(TemplateView):
    template_name = 'tickets/register.html'
    
    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'tickets/register.html', context)
    
    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
        
        context = {'user_form': user_form}
        return render(request, 'tickets/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')

def pageNotFound(request, exception):
    return render(exception, 'tickets/error404.html', {'title': 'Страница не найдена'})

