from django import template
from tickets.models import *

register = template.Library()

#cats

@register.simple_tag(name="getcats")
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('tickets/list_categories.html', name="showcats")
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}