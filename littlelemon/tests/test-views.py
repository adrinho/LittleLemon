from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_items = [
            {"title": "Burger", "price": 100, "inventory": 50},
            {"title": "Pizza", "price": 200, "inventory": 30},
            {"title": "Fries", "price": 50, "inventory": 100}
        ]
        for item in self.menu_items:
            Menu.objects.create(**item)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = MenuSerializer(self.menu_items, many=True).data
        self.assertEqual(response.data, serialized_data)
