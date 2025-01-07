from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (recipes application).
urlpatterns = [
    path('', views.menu, name='menu'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]
