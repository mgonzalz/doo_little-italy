from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (nutrition application).
urlpatterns = [
    path('', views.customize_pizza, name='customize_pizza'),
    path('summary/<int:custom_pizza_id>/', views.custom_pizza_summary, name='custom_pizza_summary'),
]
