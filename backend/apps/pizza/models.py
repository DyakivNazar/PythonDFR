from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from core.services.file_service import upload_pizza_photo
from ..pizza.managers import PizzaManager
from ..pizza_shop.models import PizzaShopModel


#     VALIDATIONS
class DaysChoices(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
        ordering = ('id',)

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)])
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100)])
    size = models.IntegerField()
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
    photo = models.ImageField(upload_to=upload_pizza_photo, blank=True)

    objects = PizzaManager()