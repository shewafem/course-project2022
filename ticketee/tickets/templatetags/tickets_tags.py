from django import template
from django.http import Http404
from tickets.models import *

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

@register.inclusion_tag('tickets/list_categories.html', name="show_cats")
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('tickets/list_events.html', name="show_events")
def show_events(cat_selected=""):
    if cat_selected:
        category = get_object_or_404(Category, slug=cat_selected)
        events_by_cat = Event.objects.filter(category_id=category.id)
        if len(events_by_cat) == 0:
            raise Http404()
        return {'events': events_by_cat}
    else:
        events = Event.objects.all()
        return {'events': events}
    