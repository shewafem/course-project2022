from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', events, name = 'events'),
    path('<slug:cat_slug>/', events_by_category, name = 'category'),
    path('<slug:cat_slug>/<slug:event_slug>/', event, name='event'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = pageNotFound