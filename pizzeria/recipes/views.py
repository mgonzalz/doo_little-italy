from django.shortcuts import render
from .models import Recipe

# Create your views here.
from django.db.models import Q

def menu(request):
    recipes = Recipe.objects.all()

    # Filtro de dieta
    diet = request.GET.get('diet')
    if diet:
        diet_query = f"(^|, )({diet})(,|$)"
        recipes = recipes.filter(healthLabels__iregex=diet_query)

    # Filtro de precio
    price = request.GET.get('price')
    if price == 'low-to-high':
        recipes = recipes.order_by('price')
    elif price == 'high-to-low':
        recipes = recipes.order_by('-price')

    # Filtro de calorias
    calories = request.GET.get('calories')
    if calories == 'low-to-high':
        recipes = recipes.order_by('calories')
    elif calories == 'high-to-low':
        recipes = recipes.order_by('-calories')

    # Filtro de busqueda por nombre o ingredientes
    search = request.GET.get('search')
    if search:
        recipes = recipes.filter(Q(name__icontains=search) | Q(ingredients__icontains=search))

    # Etiquetas Relevantes - Dietas
    labels = ["Vegetarian", "Vegan", "Gluten-Free", "Egg-Free", "Pescatarian"]

    context = {
        'recipes': recipes,
        'labels': labels,
    }
    return render(request, 'recipes/menu.html', context)

