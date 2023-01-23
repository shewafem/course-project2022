from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
import pandas as pd
from events.models import Event


from .models import *

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {'title': 'Ticketee — продажа билетов'})

def about_us(request):
    return render(request, 'main/about_us.html', {'title': 'О нас | Ticketee'})

def pageNotFound(request, exception):
    return render(exception, 'main/error_404.html', {'title': 'Страница не найдена'})

def export_data_to_excel(request):
    objs = Event.objects.all()
    data = []
    
    for obj in objs:
        data.append({
            "Название": obj.name,
            "Описание": obj.description,
            "Выступающий": obj.performer,
            "Дата": obj.date,
            "Время": obj.time,
            "Место": obj.location,
            "Цена": obj.price,
        })
    pd.DataFrame(data).to_excel('events.xlsx')
    return redirect('events')