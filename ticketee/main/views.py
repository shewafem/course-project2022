from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import *

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {'title': 'Ticketee — продажа билетов'})

def about_us(request):
    return render(request, 'main/about_us.html', {'title': 'О нас | Ticketee'})

def pageNotFound(request, exception):
    return render(exception, 'main/error_404.html', {'title': 'Страница не найдена'})