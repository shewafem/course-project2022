from django.contrib import admin

from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Customer)