from django.http import Http404
from django.shortcuts import render

from .models import *

# Create your views here.
def event(request, event_slug, cat_slug):
    event = get_object_or_404(Event, slug=event_slug)
    
    return render(request, 'events/event.html', {'event': event, 'title': event.name, 'cat_selected': cat_slug})

def events_by_category(request, cat_slug):
    category = get_object_or_404(Category, slug = cat_slug)
    context = {
        'title' : f'{category.name} | Ticketee',
        'cat_selected' : cat_slug,
    }
    
    return render(request, 'events/events_by_category.html', context=context)

def events(request):
    return render(request, 'events/events.html', {'title': 'События | Ticketee'})