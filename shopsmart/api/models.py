

from django.db import models


class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    note = models.TextField(blank=True)
    is_bought = models.BooleanField(default=False)

