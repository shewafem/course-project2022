from django import template
from tickets.models import *

register = template.Library()

#cats

@register.simple_tag(name="get_cats")
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('tickets/list_categories.html', name="show_cats")
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('tickets/list_events.html', name="show_events")
def show_events():
    events = Event.objects.all()
    return {'events': events}