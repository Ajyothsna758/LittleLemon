from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse, NoReverseMatch
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="pasta", price=44.88, inventory=5)
        Menu.objects.create(title="Badam Milk", price=12.99, inventory=9)
        #self.client=APIClient
    
    def test_getall(self):
        try:
            url= reverse("menu")
        except NoReverseMatch:
            url= "api/menu/"
        response= self.client.get(url,format="json")
        menus= Menu.objects.all()
        serialized_menus= MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_menus.data)   
                
                
        