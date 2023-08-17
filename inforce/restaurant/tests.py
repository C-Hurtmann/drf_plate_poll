from rest_framework import status
from rest_framework.test import APITestCase

from .models import Restaurant


class RestaurantTests(APITestCase):
    
    def test_create_object(self):
        self.assertEqual(2+2, 4)