from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Restaurant, Dish, Menu
from .serializers import RestaurantSerializer, DishSerializer, MenuSerializer
from .permissions import IsRestauratorOrReadOnly
# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, IsRestauratorOrReadOnly)

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticated, IsRestauratorOrReadOnly)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, IsRestauratorOrReadOnly)
