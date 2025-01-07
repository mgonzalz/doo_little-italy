from django.shortcuts import render
from .models import Recipe

# Create your views here.
def menu(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/menu.html', {"recipes": recipes})
