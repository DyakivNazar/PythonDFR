from rest_framework.test import APITestCase

from apps.pizza.models import PizzaModel
from apps.pizza_shop.models import PizzaShopModel


class PizzaShopFilterTestCase(APITestCase):
    def setUp(self):
        self.ps1 = PizzaShopModel.objects.create(name='Pizza Shop 1')
        self.pizza1 = PizzaModel.objects.create(
            name="pizza1",
            size=200,
            price=200,
            pizza_shop=self.ps1
        )
        self.pizza2 = PizzaModel.objects.create(
            name="pizza2",
            size=200,
            price=200,
            pizza_shop=self.ps1
        )
        self.pizza3 = PizzaModel.objects.create(
            name="pizza3",
            size=200,
            price=200,
            pizza_shop=self.ps1
        )