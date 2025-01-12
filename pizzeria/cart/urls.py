from django.contrib import admin
from django.urls import path, include
from . import views

# URL configuration for pizzeria project (cart application).

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:recipe_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_custom/<int:custom_pizza_id>/', views.add_custom_pizza_to_cart, name='add_custom_pizza_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:order_id>/confirmation/', views.order_confirmation, name='order_confirmation'),
    path('history/', views.order_history, name='order_history'),
    path('checkout-errors/', views.checkout_error, name='checkout_errors'),
]
