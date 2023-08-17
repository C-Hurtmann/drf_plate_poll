from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Dish, Restaurant, Menu

User = get_user_model()

HOST = 'http://127.0.0.1/api/v1'

class RestaurantWithRestaurateurUserTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='res1', password='restpass', role='restaurateur')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.restaurant = Restaurant.objects.create(name='Restaurant 1', user=self.user)
        self.dish = Dish.objects.create(name='Dish 1', description='Delicious dish', price='9.99', user=self.user)
        self.menu = Menu.objects.create(restaurant=self.restaurant, day_of_week=1, user=self.user)
        self.menu.dishes.add(self.dish)

    def test_retrieve_restaurant_list(self):
        response = self.client.get(HOST + '/restaurant/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_restaurant_with_authenticated_user(self):
        data = {
            'name': 'New Restaurant',
        }
        response = self.client.post(HOST + '/restaurant/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 2)

    def test_retrieve_dish_list(self):
        response = self.client.get(HOST + '/restaurant/dish/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dish_with_authenticated_user(self):
        data = {
            'name': 'New Dish',
            'description': 'Delicious new dish',
            'price': '10.99',
        }
        response = self.client.post(HOST + '/restaurant/dish/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 2)

    def test_retrieve_menu(self):
        response = self.client.get(HOST + '/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_with_authenticated_user(self):
        data = {
            'restaurant': self.restaurant.id,
            'day_of_week': 2,
            'dishes': [self.dish.id],
        }
        response = self.client.post(HOST + '/restaurant/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)


class RestaurantDishMenuViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_restaurant_list_without_authentication(self):
        response = self.client.get(HOST + '/restaurant/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_restaurant_without_authenticated_user(self):
        data = {
            'name': 'New Restaurant',
        }
        response = self.client.post(HOST + '/restaurant/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Restaurant.objects.count(), 0)

    def test_retrieve_dish_list_without_authentication(self):
        response = self.client.get(HOST + '/restaurant/dish/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_dish_without_authenticated_user(self):
        data = {
            'name': 'New Dish',
            'description': 'Delicious new dish',
            'price': '10.99',
        }
        response = self.client.post(HOST + '/restaurant/dish/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Dish.objects.count(), 0)

    def test_retrieve_menu_list_without_authentication(self):
        response = self.client.get(HOST + '/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_menu_without_authenticated_user(self):
        data = {
            'restaurant': 1,
            'day_of_week': 2,
            'dishes': [1],
        }
        response = self.client.post(HOST + '/restaurant/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Menu.objects.count(), 0)


class RestaurantWithEmployeeUserTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='emp1', password='restpass', role='employee')
        self.restaurateur = User.objects.create_user(username='res1', password='restpass', role='restaurateur')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.restaurant = Restaurant.objects.create(name='Restaurant 1', user=self.restaurateur)
        self.dish = Dish.objects.create(name='Dish 1', description='Delicious dish', price='9.99', user=self.restaurateur)
        self.menu = Menu.objects.create(restaurant=self.restaurant, day_of_week=1, user=self.restaurateur)
        self.menu.dishes.add(self.dish)

    def test_retrieve_restaurant_list(self):
        response = self.client.get(HOST + '/restaurant/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_restaurant_with_authenticated_user(self):
        data = {
            'name': 'New Restaurant',
        }
        response = self.client.post(HOST + '/restaurant/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Restaurant.objects.count(), 1)

    def test_retrieve_dish_list(self):
        response = self.client.get(HOST + '/restaurant/dish/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dish_with_authenticated_user(self):
        data = {
            'name': 'New Dish',
            'description': 'Delicious new dish',
            'price': '10.99',
        }
        response = self.client.post(HOST + '/restaurant/dish/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Dish.objects.count(), 1)

    def test_retrieve_menu(self):
        response = self.client.get(HOST + '/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_with_authenticated_user(self):
        data = {
            'restaurant': self.restaurant.id,
            'day_of_week': 2,
            'dishes': [self.dish.id],
        }
        response = self.client.post(HOST + '/restaurant/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Menu.objects.count(), 1)
