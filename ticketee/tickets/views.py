from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import *

def home(request):
    events = Event.objects.all()
    
    context = {
        'events': events,
        'title' : 'Ticketee — продажа билетов',
        'cat_selected' : 0,
    }
    
    return render(request, 'tickets/home.html', context = context)

def about(request):
    return render(request, 'tickets/about.html', {'title': 'О нас | Ticketee'})

def show_event(request, event_id, cat_id):
    event = get_object_or_404(Event, id=event_id)
    
    return render(request, 'tickets/event.html', {'event': event, 'title': event.name, 'cat_selected': cat_id})

def show_events_by_category(request, cat_id):
    events_by_cats = Event.objects.filter(category_id=cat_id)
    
    if len(events_by_cats) == 0:
        raise Http404()
    
    context = {
        'events': events_by_cats,
        'title' : 'Ticketee — продажа билетов',
        'cat_selected' : cat_id,
    }
    
    return render(request, 'tickets/events_by_category.html', context=context)

def pageNotFound(request, exception):
    return render(exception, 'tickets/error404.html', {'title': 'Страница не найдена'})