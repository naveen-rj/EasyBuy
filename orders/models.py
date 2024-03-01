from django.db import models
from customers.models import Customer
from products.models import Product

# Model for Orders
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_CANCELLED = 4
    STATUS_CHOICES = ((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                      (ORDER_PROCESSED,'ORDER_PROCESSED'),
                      (ORDER_DELIVERED,'ORDER_DELIVERED'),
                      (ORDER_CANCELLED,'ORDER_CANCELLED'))
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Model for Ordered Items
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='ordered_items')
    quantity = models.IntegerField(default=1)

