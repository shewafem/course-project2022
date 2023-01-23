from modeltranslation.translator import register, TranslationOptions, translator

from .models import *

@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
    