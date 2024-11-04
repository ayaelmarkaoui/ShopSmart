from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShoppingListViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'shoppinglists', ShoppingListViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
