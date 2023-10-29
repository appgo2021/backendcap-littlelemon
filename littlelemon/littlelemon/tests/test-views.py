from django.tests import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.data={
            "user": "test",
            "email":"test@12.com",
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    def test_getall(self):
        return Menu.objects.all()