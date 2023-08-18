from django.urls import path, include
from rest_framework import routers

from .views import RestaurantViewSet, DishViewSet, MenuViewSet


router = routers.SimpleRouter()

router.register(r"dish", DishViewSet, basename="dish")
router.register(r"menu", MenuViewSet, basename="menu")
router.register(r"", RestaurantViewSet, basename="restaurant")


urlpatterns = [path("restaurant/", include(router.urls))]
