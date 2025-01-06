from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (authentication application).
urlpatterns = [
    path('', views.UserProfileView.as_view(), name='user-profile'),
]
