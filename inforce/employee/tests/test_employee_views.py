import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

from employee.models import Vote
from restaurant.models import Restaurant, Dish, Menu

User = get_user_model()

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def test_user():
    return User.objects.create_user(
        username="emp1", password="test123", role="employee"
    )

@pytest.fixture
def menus(api_client):
    restaurateur = User.objects.create_user(
        username="res1", password="test123", role="restaurateur"
    )
    
    restaurant1 = Restaurant.objects.create(name="Pasta & Pizza", user=restaurateur)
    restaurant2 = Restaurant.objects.create(name="Granat", user=restaurateur)
    
    dish1 = Dish.objects.create(
        name="Cheese pizza", description="with cheese", price="15.99", user=restaurateur
    )
    dish2 = Dish.objects.create(
        name="Pepperoni pizza", description="with pepperoni", price="16.99", user=restaurateur
    )
    dish3 = Dish.objects.create(
        name="Steak", description="Medium rare", price="20", user=restaurateur
    )
    menu1 = Menu.objects.create(
        restaurant=restaurant1, day_of_week=2, user=restaurateur
    )
    menu2 = Menu.objects.create(
        restaurant=restaurant2, day_of_week=2, user=restaurateur
    )
    menu1.dishes.set([dish1, dish2])
    menu2.dishes.set([dish3])
    return (menu1, menu2)

@pytest.mark.django_db
def test_create_vote_rastaurant_forbidden(api_client, test_user):
    api_client.force_authenticate(user=test_user)

    restaurant = Restaurant.objects.create(name="Restaurant 1", user=test_user)
    dish = Dish.objects.create(
        name="Dish 1", description="Delicious dish", price="9.99", user=test_user
    )

    url = reverse("menu-list")
    data = {
        "restaurant": restaurant.id,
        "day_of_week": 2,
        "dishes": [dish.id],
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_create_vote(api_client, test_user, menus):
    api_client.force_authenticate(user=test_user)
    url = reverse("vote-list")
    data = {"menu": menus[0].id}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Vote.objects.get().menu == menus[0]
