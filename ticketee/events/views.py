from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.

def event(request, event_slug, cat_slug):
    event = get_object_or_404(Event, slug=event_slug)

    context = {'event': event, 'title': event.name, 'cat_slug': cat_slug}
    return render(request, 'events/event.html', context)

def events_by_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    context = {
        'title': f'{category.name} | Ticketee',
        'cat_selected': cat_slug,
    }

    return render(request, 'events/events_by_category.html', context=context)


def events(request):
    return render(request, 'events/events.html', {'title': 'События | Ticketee'})


def my_events(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    context = {'order': order, 'title': 'Мои билеты | Ticketee'}
    return render(request, 'events/my_events.html', context)

def add_to_my_events(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    if request.method == 'POST':
        event = Event.objects.get(slug=event_slug)
		#Get user account information
        try:
            customer = request.user.customer	
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, event=event)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('my-events')

    context = {'event': event, 'title': event.name}
    return render(request, 'events/event.html', context)

def create_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddEventForm()
    context = {'form': form, 'title': 'Добавить новое событие', 'action': 'Добавить'}
    return render(request, 'events/create_event.html', context)

def update_event(request, pk):
    event = Event.objects.get(pk = pk)
    form = AddEventForm(instance = event)
    
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'title': 'Редактировать событие', 'action': 'Сохранить', 'event': event}
    return render(request, 'events/update_event.html', context)

def delete_event(request, pk):
    event = Event.objects.get(pk = pk)
    event.delete()
    return redirect('events')
#def remove_from_my_events(request, event_slug):
    