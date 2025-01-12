from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ingredient, CustomPizza

# Create your views here.
@login_required
def customize_pizza(request):
    bases = Ingredient.objects.filter(category='Base')
    sauces = Ingredient.objects.filter(category='Sauce')
    toppings = Ingredient.objects.filter(category='Topping')

    if request.method == 'POST':
        selected_base_id = request.POST.get('base')
        selected_sauce_id = request.POST.get('sauce')
        selected_toppings_ids = request.POST.getlist('toppings')
        pizza_name = request.POST.get('name', 'Custom Pizza')

        # Obtener los ingredientes seleccionados
        selected_base = Ingredient.objects.get(id=selected_base_id).name
        selected_sauce = Ingredient.objects.get(id=selected_sauce_id).name
        selected_toppings = [Ingredient.objects.get(id=t).name for t in selected_toppings_ids]

        # Calcular el precio total
        base_price = 12.0
        total_price = base_price
        total_calories = 0

        base_price += Ingredient.objects.get(id=selected_base_id).price_per_unit
        total_calories += Ingredient.objects.get(id=selected_base_id).calories_per_unit

        sauce_price = Ingredient.objects.get(id=selected_sauce_id).price_per_unit
        sauce_calories = Ingredient.objects.get(id=selected_sauce_id).calories_per_unit
        total_price += sauce_price
        total_calories += sauce_calories

        for topping_id in selected_toppings_ids:
            topping = Ingredient.objects.get(id=topping_id)
            total_price += topping.price_per_unit
            total_calories += topping.calories_per_unit

        # Crear la pizza personalizada
        custom_pizza = CustomPizza.objects.create(
            user=request.user,
            name=pizza_name,
            base=selected_base,
            sauce=selected_sauce,
            toppings=', '.join(selected_toppings),
            calories=total_calories,
            price=total_price
        )
        return redirect('custom_pizza_summary', custom_pizza_id=custom_pizza.id)

    return render(request, 'nutrition/customize.html', {
        'bases': bases,
        'sauces': sauces,
        'toppings': toppings,
    })

@login_required
def custom_pizza_summary(request, custom_pizza_id):
    custom_pizza = get_object_or_404(CustomPizza, id=custom_pizza_id, user=request.user)
    return render(request, 'nutrition/summary.html', {
        'custom_pizza': custom_pizza
    })
