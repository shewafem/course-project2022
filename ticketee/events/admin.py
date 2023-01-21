from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date', 'is_available', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('is_available',)
    list_filter = ('is_available', )
    save_on_top = True
    
    readonly_fields = ('get_html_photo',)
    
    
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")
    
    get_html_photo.short_description = "Миниатюра"
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Customer)