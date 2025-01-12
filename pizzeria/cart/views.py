from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, Order, OrderItem
from recipes.models import Recipe
from nutrition.models import CustomPizza
import stripe
from django.conf import settings

# Create your views here.
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, recipe=recipe)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def add_custom_pizza_to_cart(request, custom_pizza_id):
    custom_pizza = get_object_or_404(CustomPizza, id=custom_pizza_id)

    # Crea o actualiza el elemento en el carrito
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        custom_pizza=custom_pizza,
        recipe=None  # Asegura que es una pizza personalizada
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = new_quantity
        cart_item.save()
    return redirect('cart_view')


stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart_view')

    # Crear el pedido antes de iniciar la sesión de Stripe
    order = Order.objects.create(user=request.user)

    # Crear líneas de pedido para Stripe
    line_items = []
    for item in cart_items:
        if item.recipe:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.recipe.name,
                    },
                    'unit_amount': int(item.recipe.price * 100),
                },
                'quantity': item.quantity,
            })
            OrderItem.objects.create(order=order, recipe=item.recipe, quantity=item.quantity)
        elif item.custom_pizza:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.custom_pizza.name,
                    },
                    'unit_amount': int(item.custom_pizza.price * 100),
                },
                'quantity': item.quantity,
            })
            OrderItem.objects.create(order=order, custom_pizza=item.custom_pizza, quantity=item.quantity)

    # Crear la sesión de pago en Stripe
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(f'/cart/order/{order.id}/confirmation/'),
            cancel_url=request.build_absolute_uri('/cart/'),
        )
        # Vaciar el carrito
        cart_items.delete()
        return redirect(checkout_session.url)
    except Exception as e:
        return render(request, 'cart/checkout_error.html', {'error': str(e)})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/order_confirmation.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cart/order_history.html', {'orders': orders})


def checkout_error(request):
    return render(request, 'cart/checkout_error.html')
