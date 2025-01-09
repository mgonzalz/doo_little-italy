from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.recipe.price * self.quantity

    def __str__(self):
        return f"{self.recipe.name} - {self.quantity} pcs"
