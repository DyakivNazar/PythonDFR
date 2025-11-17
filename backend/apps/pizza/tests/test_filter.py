from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.pizza.models import PizzaModel
from apps.pizza_shop.models import PizzaShopModel


class PizzaFilterTestCase(APITestCase):
    def setUp(self):
        pizza_shop = PizzaShopModel.objects.create(name='Pizza Shop')

        self.p1 = PizzaModel.objects.create(
            name="Margherita",
            size=20,
            price=100,
            pizza_shop=pizza_shop
        )
        self.p2 = PizzaModel.objects.create(
            name="Pepperoni",
            size=30,
            price=200,
            pizza_shop=pizza_shop
        )
        self.p3 = PizzaModel.objects.create(
            name="Hawaiian",
            size=40,
            price=300,
            pizza_shop=pizza_shop
        )
        self.p4 = PizzaModel.objects.create(
            name="MegaPizza",
            size=50,
            price=2000,
            pizza_shop=pizza_shop
        )

        self.url = reverse('pizza_list_create')

    def _get(self, params):
        return self.client.get(self.url, params)

    def test_price_lt(self):
        res = self._get({'price_lt': 200})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)

    def test_price_gt(self):
        res = self._get({'price_gt': 200})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)

    def test_price_lte(self):
        res = self._get({'price_lte': 200})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)

    def test_price_gte(self):
        res = self._get({'price_gte': 200})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)

    def test_size_lt(self):
        res = self._get({'size_lt': 40})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)

    def test_size_gt(self):
        res = self._get({'size_gt': 40})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)

    def test_size_lte(self):
        res = self._get({'size_lte': 40})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)

    def test_size_gte(self):
        res = self._get({'size_gte': 40})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)

    def test_name_start(self):
        res = self._get({'name_start': 'H'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(res.data['data'][0]['name'], self.p3.name)

    def test_name_contains(self):
        res = self._get({'name_contains': 'r'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        pizza_names = ['Margherita', 'Pepperoni']
        for i, pizza in enumerate(res.data['data']):
            self.assertEqual(pizza['name'], pizza_names[i])

    def test_name_end(self):
        res = self._get({'name_end': 'i'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(res.data['data'][0]['name'], self.p2.name)


    def test_range(self):
        res = self._get({'range_min': 30, 'range_max': 50})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)
        range = [30,40,50]
        for i, pizza in enumerate(res.data['data']):
            self.assertEqual(pizza['size'], range[i])

    def test_price_in(self):
        res = self._get({'price_in': '100, 300, 2000'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)
        price_in = [100, 300, 2000]
        for i, pizza in enumerate(res.data['data']):
            self.assertEqual(pizza['price'], price_in[i])

    def test_order_price_desc(self):
        res = self._get({'order': '-price'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['data'][0]['id'], self.p4.pk)

    def test_order_name_desc(self):
        res = self._get({'order': '-name'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['data'][0]['id'], self.p2.pk)





