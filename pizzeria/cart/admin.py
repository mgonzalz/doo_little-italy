from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No añadir filas adicionales por defecto

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'total_price')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]  # Mostrar los elementos del pedido en línea
    readonly_fields = ('user',)  # Hacer que el campo 'user' no sea editable

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Total Price ($)'
