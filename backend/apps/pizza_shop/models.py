from django.db import models

class PizzaShopModel(models.Model):
    class Meta:
        db_table = 'pizza_shop'

    name = models.CharField(max_length=100)