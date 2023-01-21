from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        
    class Meta:
        model = Event
        fields = ['name', 'slug', 'category', 'description', 'photo', 'location', 'performer', 'date', 'time', 'quantity', 'price']
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов!')
        return name
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise ValidationError('Должен быть хотя бы один билет!')
        return quantity
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной!')
        return price