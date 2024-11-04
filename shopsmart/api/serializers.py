from rest_framework import serializers
from .models import ShoppingList, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShoppingListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = '__all__'
