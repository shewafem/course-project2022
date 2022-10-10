from http.client import HTTPResponse
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import *

class EventHome(ListView):
    model = Event
    template_name = 'tickets/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ticketee — продажа билетов'
        context['cat_selected'] = ""
        
        return context
    
def events(request):
    return render(request, 'tickets/events.html')

def about(request):
    return render(request, 'tickets/about.html', {'title': 'О нас | Ticketee'})

def show_event(request, event_slug, cat_slug):
    event = get_object_or_404(Event, slug=event_slug)
    
    return render(request, 'tickets/event.html', {'event': event, 'title': event.name, 'cat_selected': cat_slug})

def show_events_by_category(request, cat_slug):
    category = get_object_or_404(Category, slug = cat_slug)
    context = {
        'title' : f'Ticketee — продажа билетов | {category.name}',
        'cat_selected' : cat_slug,
    }
    
    return render(request, 'tickets/events_by_category.html', context=context)

def auth(request):
    return render(request, 'tickets/auth.html')

def pageNotFound(request, exception):
    return render(exception, 'tickets/error404.html', {'title': 'Страница не найдена'})

