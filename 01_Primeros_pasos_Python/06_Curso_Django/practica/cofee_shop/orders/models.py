from django.db import models
from django.contrib.auth.models import User

from products.models import Products


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.id} by {self.user}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.PROTECT) ## Si la orden esta lista no borren esos datos es para proteher esos datos 
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.order} - {self.product}"