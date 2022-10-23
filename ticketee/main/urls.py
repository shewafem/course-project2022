from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = pageNotFound