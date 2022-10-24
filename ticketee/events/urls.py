from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', events, name = 'events'),
    path('my-events/', my_events, name='my-events'),
    path('<slug:cat_slug>/', events_by_category, name = 'category'),
    path('<slug:cat_slug>/<slug:event_slug>/', event, name='event'),
    path('my-events/orders/<slug:event_slug>/', add_to_my_events, name='add-to-my-events')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = pageNotFound