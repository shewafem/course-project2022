from django.conf import settings

from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)