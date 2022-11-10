"""SakshiShowroom URL Configuration """
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="homepage"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('login',views.login, name="loginpage"),
    path('logout',views.logout),
]
