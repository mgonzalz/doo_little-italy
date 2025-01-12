from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
from nutrition.models import CustomPizza
# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    custom_pizza = models.ForeignKey(CustomPizza, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        if self.recipe:
            return self.recipe.price * self.quantity
        elif self.custom_pizza:
            return self.custom_pizza.price * self.quantity
        return 0

    def __str__(self):
        if self.recipe:
            return f"{self.recipe.name} - {self.quantity} pcs"
        elif self.custom_pizza:
            return f"{self.custom_pizza.name} - {self.quantity} pcs"


## Modelos para hacer el checkout.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending',
    )
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def total_price(self):
        return sum(item.total_price() for item in self.order_items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    custom_pizza = models.ForeignKey(CustomPizza, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        if self.recipe:
            return self.recipe.price * self.quantity
        elif self.custom_pizza:
            return self.custom_pizza.price * self.quantity
        return 0

    def __str__(self):
        if self.recipe:
            return f"{self.recipe.name} ({self.quantity})"
        elif self.custom_pizza:
            return f"{self.custom_pizza.name} ({self.quantity})"
