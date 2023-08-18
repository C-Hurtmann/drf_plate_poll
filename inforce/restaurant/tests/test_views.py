import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings

from restaurant.models import Restaurant, Dish, Menu

User = get_user_model()

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def test_user():
    return User.objects.create_user(
        username="res1", password="test123", role="restaurateur"
    )
@pytest.fixture
def test_user_two():
    return User.objects.create_user(
        username="res2", password="test123", role="restaurateur"
    )

@pytest.mark.django_db
def test_create_restaurant(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    url = reverse("restaurant-list")
    data = {"name": "New Restaurant"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.count() == 1
    assert Restaurant.objects.get().name == "New Restaurant"

@pytest.mark.django_db
def test_create_dish(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    url = reverse("dish-list")
    data = {"name": "New Dish", "description": "Delicious new dish", "price": "10.99"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Dish.objects.count() == 1
    assert Dish.objects.get().name == "New Dish"

@pytest.mark.django_db
def test_create_menu(api_client, test_user):
    restaurant = Restaurant.objects.create(name="Restaurant 1", user=test_user)
    dish = Dish.objects.create(
        name="Dish 1", description="Delicious dish", price="9.99", user=test_user
    )

    api_client.force_authenticate(user=test_user)
    url = reverse("menu-list")
    data = {
        "restaurant": restaurant.id,
        "day_of_week": 2,
        "dishes": [dish.id],
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Menu.objects.count() == 1
    assert Menu.objects.get().day_of_week == 2
