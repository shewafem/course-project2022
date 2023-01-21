from msilib.schema import Property
from django.db import models

# Create your models here.
from django.urls import reverse
from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)
    
    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ['id']

class Event(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    description = models.TextField('Описание', help_text='Подробно опишите событие и расскажите про выступающих')
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    performer = models.CharField('Выступающий', max_length=255)
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name='Категория')
    location = models.CharField('Место', max_length=255)
    is_available = models.BooleanField('Доступность', default=True)
    quantity = models.IntegerField('Количество билетов')
    price = models.IntegerField('Цена')
    photo = models.ImageField('Фото', upload_to="photos/events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_slug': self.slug, 'cat_slug':self.category.slug})

    @property
    def photoURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['date']


class Category(models.Model):
    name = models.CharField("Название", max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name="URL", db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id']


class OrderItem(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.event.price * self.quantity
        return total

    class Meta:
        verbose_name = 'Бронирование события'
        verbose_name_plural = 'Бронирования событий'
        ordering = ['id']
