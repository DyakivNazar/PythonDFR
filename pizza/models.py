from django.db import models

class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizza'
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.IntegerField()