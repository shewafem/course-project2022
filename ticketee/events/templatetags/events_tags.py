from django import template
from django.http import Http404
from events.models import *

register = template.Library()

#cats

@register.simple_tag(name="get_cats")
def get_categories():
    return Category.objects.all()

@register.simple_tag(name="get_events")
def get_events(filter=None):
    if not filter:
        return Event.objects.all()
    else:
        return Event.objects.filter(category_id = filter)

@register.inclusion_tag('events/categories_list.html', name="show_cats")
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('events/events_list.html', name="show_events")
def show_events(cat_selected=""):
    if cat_selected:
        events = Event.objects.filter(category__slug=cat_selected)
        if len(events) == 0:
            raise Http404()
        return {'events': events}
    else:
        events = Event.objects.all()
        return {'events': events}