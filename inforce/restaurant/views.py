from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Restaurant, Dish, Menu
from .serializers import RestaurantSerializer, DishSerializer, MenuSerializer
from .permissions import IsRestauratorOrReadOnly, IsOwner
# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, IsRestauratorOrReadOnly, IsOwner)
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'restaurateur':
            return Restaurant.objects.filter(user=user)
        return Restaurant.objects.all()

class DishViewSet(viewsets.ModelViewSet):
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticated, IsRestauratorOrReadOnly, IsOwner)
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'restaurateur':
            return Dish.objects.filter(user=user)
        return Dish.objects.all()

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, IsRestauratorOrReadOnly, IsOwner)
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'restaurateur':
            return Menu.objects.filter(user=user)
        return Menu.objects.all()