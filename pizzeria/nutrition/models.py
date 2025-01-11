from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    CATEGORY_CHOICES = [
        ('Base', 'Base'),
        ('Sauce', 'Sauce'),
        ('Topping', 'Topping'),
    ]

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Topping')
    calories_per_unit = models.FloatField(default=0)
    fats_per_unit = models.FloatField(default=0)
    proteins_per_unit = models.FloatField(default=0)
    carbohydrates_per_unit = models.FloatField(default=0)
    price_per_unit = models.FloatField(default=0)
    unit = models.CharField(max_length=50, default="grams")

    def __str__(self):
        return f"{self.name} ({self.category})"


class CustomPizza(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='custom_pizzas')
    name = models.CharField(max_length=255, default="Custom Pizza")
    base = models.CharField(max_length=100)
    sauce = models.CharField(max_length=100)
    toppings = models.TextField()
    calories = models.FloatField(default=0)
    price = models.FloatField(default=12.0)

    def __str__(self):
        return f"{self.name} by {self.user.username}"
