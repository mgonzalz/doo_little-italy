from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (core application).
urlpatterns = [
    path('about/', views.about, name='about'),
]
