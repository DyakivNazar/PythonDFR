import os

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.pizza.models import PizzaModel
from apps.pizza_shop.models import PizzaShopModel
from configs import settings
from core.dataclasses.user_dataclasse import User

UserModel = get_user_model()


class PizzaAPITestCase(APITestCase):
    def setUp(self):
        self.pizza_shop = PizzaShopModel.objects.create(name='Pizza Shop')
        self.pizza1 = PizzaModel.objects.create(
            name="pizza1",
            size=200,
            price=200,
            pizza_shop=self.pizza_shop
        )
        self.pizza2 = PizzaModel.objects.create(
            name="pizza2",
            size=200,
            price=200,
            pizza_shop=self.pizza_shop
        )
        self.pizza3 = PizzaModel.objects.create(
            name="pizza3",
            size=200,
            price=200,
            pizza_shop=self.pizza_shop
        )

    def _authenticate(self):
        user: User = UserModel.objects.create_user(email='admin@gmail.com', password='admin')
        user.is_active = True
        user.save()
        res = self.client.post(reverse('auth_login'), {'email': user.email, 'password': 'admin'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + res.data['access'])

    def test_get_all_pizzas(self):
        res = self.client.get(reverse('pizza_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)
        pizza_names = ['pizza1', 'pizza2', 'pizza3']
        for i, pizza in enumerate(PizzaModel.objects.all()):
            self.assertEqual(pizza.name, pizza_names[i])

    def test_create_pizza_without_auth(self):
        count_before = PizzaModel.objects.count()
        res = self.client.post(reverse('pizza_list_create'), data={
            'name': 'asd',
            'size': 200,
            'price': 2000,
        })
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        count_after = PizzaModel.objects.count()
        self.assertEqual(count_after - count_before, 0)

    def test_create_pizza_with_auth(self):
        self._authenticate()
        count_before = PizzaModel.objects.count()
        res = self.client.post(reverse('pizza_list_create'), data={
            'name': 'Asd',
            'size': 100,
            'price': 2000,
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        count_after = PizzaModel.objects.count()
        self.assertEqual(count_after - count_before, 1)
        self.assertEqual(res.data['name'], 'Asd')

    def test_update_pizza_with_put(self):
        res = self.client.put(reverse('pizza_id_get_put_del', args=[self.pizza1.pk]),
                              data={
                                  'name': 'Pizza',
                                  'size': 20,
                                  'price': 2000,
                              }
                              )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_pizza(self):
        res = self.client.delete(reverse('pizza_id_get_put_del', args=[self.pizza1.pk]))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_pizza_by_id(self):
        res = self.client.get(reverse('pizza_id_get_put_del', args=[self.pizza1.pk]))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['size'], 200)

    # def test_add_photo_to_pizza(self):
    #     path = os.path.join(settings.BASE_DIR, "apps/pizza/tests/data/pizza.jpg")
    #
    #     with open(path, "rb") as f:
    #         image = SimpleUploadedFile(
    #             "pizza.jpg",
    #             f.read(),
    #             content_type="image/jpeg"
    #         )
    #
    #     res = self.client.patch(
    #         reverse('pizza_photo_add', args=[self.pizza1.pk]),
    #         data={"photo": image},
    #         format="multipart",
    #     )
    #     print(res.data, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

