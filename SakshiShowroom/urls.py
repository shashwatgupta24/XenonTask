"""SakshiShowroom URL Configuration """
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('', include('Showroom.urls')),
    path("admin", admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
