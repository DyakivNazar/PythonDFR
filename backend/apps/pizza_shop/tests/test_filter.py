from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.pizza.models import PizzaModel
from apps.pizza_shop.models import PizzaShopModel


class PizzaShopFilterTestCase(APITestCase):
    def setUp(self):
        self.ps1 = PizzaShopModel.objects.create(name='Napoletana')
        self.ps2 = PizzaShopModel.objects.create(name='Kara')
        self.pizza1 = PizzaModel.objects.create(
            name="Margherita",
            size=10,
            price=200,
            pizza_shop=self.ps1
        )
        self.pizza2 = PizzaModel.objects.create(
            name="Pepperoni",
            size=90,
            price=100,
            pizza_shop=self.ps1
        )
        self.pizza3 = PizzaModel.objects.create(
            name="Hawaiian",
            size=50,
            price=50,
            pizza_shop=self.ps1
        )
        self.pizza4 = PizzaModel.objects.create(
            name="MegaPizza",
            size=80,
            price=150,
            pizza_shop=self.ps2
        )

        self.url = reverse('pizza_shop_list_create')

    def _get(self, params):
        return self.client.get(self.url, params)

    def test_price_lt(self):
        res = self._get({'price_lt': 120})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 2)

    def test_price_gt(self):
        res = self._get({'price_gt': 120})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 1)
        self.assertEqual(len(res.data['data'][1]['pizzas']), 1)


    def test_price_lte(self):
        res = self._get({'price_lte': 150})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 2)
        self.assertEqual(len(res.data['data'][1]['pizzas']), 1)


    def test_price_gte(self):
        res = self._get({'price_gte': 150})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 1)
        self.assertEqual(len(res.data['data'][1]['pizzas']), 1)


    def test_size_lt(self):
        res = self._get({'size_lt': 40})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 1)


    def test_size_gt(self):
        res = self._get({'size_gt': 40})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 2)
        self.assertEqual(len(res.data['data'][1]['pizzas']), 1)


    def test_size_lte(self):
        res = self._get({'size_lte': 50})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 2)


    def test_size_gte(self):
        res = self._get({'size_gte': 50})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 2)
        self.assertEqual(len(res.data['data'][1]['pizzas']), 1)

    def test_name_start(self):
        res = self._get({'name_start': 'N'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)

    def test_name_contains(self):
        res = self._get({'name_contains': 'r'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)

    def test_name_end(self):
        res = self._get({'name_end': 'a'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)

    def test_order_name_desc(self):
        res = self._get({'order': 'name'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['data'][0]['id'], self.ps2.pk)

    def test_pizza_name_start(self):
        res = self._get({'pizza_name_start': 'H'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(res.data['data'][0]['pizzas'][0]['name'], self.pizza3.name)

    def test_pizza_name_contains(self):
        res = self._get({'pizza_name_contains': 'r'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 2)
        pizza_names = ['Margherita', 'Pepperoni']
        for i, pizza in enumerate(res.data['data'][0]['pizzas']):
            self.assertEqual(pizza['name'], pizza_names[i])

    def test_pizza_name_end(self):
        res = self._get({'pizza_name_end': 'i'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(res.data['data'][0]['pizzas'][0]['name'], self.pizza2.name)

    def test_order_pizza_name_desc(self):
        res = self._get({'order_pizzas': '-name'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['data'][0]['pizzas'][0]['id'], self.pizza2.pk)

    def test_order_price_desc(self):
        res = self._get({'order_pizzas': '-price'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['data'][0]['pizzas'][0]['id'], self.pizza1.pk)