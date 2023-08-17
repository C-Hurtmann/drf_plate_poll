from django.urls import path, include
from rest_framework import routers

from .views import RestaurantViewSet, DishViewSet, MenuViewSet


router = routers.SimpleRouter()

router.register(r'dish', DishViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'', RestaurantViewSet)




urlpatterns = [
    path('restaurant/', include(router.urls))
    ]
