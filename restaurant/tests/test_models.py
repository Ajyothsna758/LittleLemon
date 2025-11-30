from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item= Menu.objects.create(title="Falooda", price=str(45.88), inventory=8)
        self.assertEqual(str(item), "Falooda: 45.88")