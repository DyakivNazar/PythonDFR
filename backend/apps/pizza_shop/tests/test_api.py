from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.pizza.models import PizzaModel
from apps.pizza_shop.models import PizzaShopModel


class PizzaShopTestCase(APITestCase):
    def setUp(self):
        self.ps1 = PizzaShopModel.objects.create(name='Pizza Shop 1')
        self.ps2 = PizzaShopModel.objects.create(name='Pizza Shop 2')
        self.ps3 = PizzaShopModel.objects.create(name='Pizza Shop 3')
        self.ps4 = PizzaShopModel.objects.create(name='Pizza Shop 4')
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

    def test_get_all_shop(self):
        res = self.client.get(reverse('pizza_shop_list_create'), query_params={'size': 10, 'order': 'id'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 4)
        self.assertEqual(len(res.data['data'][0]['pizzas']), 3)

    def test_post_pizza_shop(self):
        count_before = PizzaShopModel.objects.count()
        res = self.client.post(reverse('pizza_shop_list_create'), data={
            'name': 'Pizza Shop 5',
        })
        count_after = PizzaShopModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_after - count_before, 1)
        self.assertEqual(res.data['name'], 'Pizza Shop 5')

    def test_add_pizza_shop2(self):
        res = self.client.post(reverse('pizza_shop_create_pizza', args=[self.ps2.pk]),
                               data={
                                   'name': 'Sara',
                                   'size': 20,
                                   'price': 500,
                               })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['pizzas'][0]['name'], 'Sara')