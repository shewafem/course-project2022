from enum import unique
from unittest.util import _MAX_LENGTH
from django.shortcuts import get_object_or_404
from django.urls import reverse
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

class Event(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField('Описание')
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    performer = models.CharField('Выступающий', max_length=255)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    location = models.CharField('Место', max_length=255)
    available = models.BooleanField('Доступность', default=True)
    price = models.IntegerField('Цена')
    photo = models.ImageField(upload_to = "photos/events")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        category = get_object_or_404(Category, id = self.category_id)
        return reverse('event', kwargs={'event_slug': self.slug, 'cat_slug': category.slug})
    
    
    class Meta:
        verbose_name= 'Событие'
        verbose_name_plural = 'События'
        ordering = ['id']
        
class Category(models.Model):
    name = models.CharField("Название", max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']