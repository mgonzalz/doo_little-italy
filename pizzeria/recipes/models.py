from django.db import models

# Create your models here.
class Recipe(models.Model): # Info: https://developer.edamam.com/edamam-docs-recipe-api
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=2000)
    healthLabels = models.TextField()
    cuisineType = models.TextField()
    calories = models.FloatField()
    totalNutrients = models.JSONField()
    ingredients = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
