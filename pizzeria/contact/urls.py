from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (contact application).
urlpatterns = [
    path('', views.contact, name='contact'),
    path('home-service/', views.home_service, name='home-service'),
]
