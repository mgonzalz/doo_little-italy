from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (core application).
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
