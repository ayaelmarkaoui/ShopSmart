from django.shortcuts import render
from rest_framework import viewsets
from .models import ShoppingList, Product
from .serializers import ShoppingListSerializer, ProductSerializer

class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

