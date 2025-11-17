from django_filters import rest_framework as filters

from .models import PizzaShopModel
from .serializer import PizzaShopSerializer


class PizzaShopFilter(filters.FilterSet):
    # фільтруємо по пов'язаній моделі Pizza (related_name='pizzas')
    price_lt = filters.NumberFilter(field_name='pizzas__price', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='pizzas__price', lookup_expr='gt')
    price_lte = filters.NumberFilter(field_name='pizzas__price', lookup_expr='lte')
    price_gte = filters.NumberFilter(field_name='pizzas__price', lookup_expr='gte')

    size_lt = filters.NumberFilter(field_name='pizzas__size', lookup_expr='lt')
    size_gt = filters.NumberFilter(field_name='pizzas__size', lookup_expr='gt')
    size_lte = filters.NumberFilter(field_name='pizzas__size', lookup_expr='lte')
    size_gte = filters.NumberFilter(field_name='pizzas__size', lookup_expr='gte')

    name_start = filters.CharFilter(field_name='name', lookup_expr='startswith')
    name_contains = filters.CharFilter(field_name='name', lookup_expr='contains')
    name_end = filters.CharFilter(field_name='name', lookup_expr='endswith')

    pizza_name_start = filters.CharFilter(field_name='pizzas__name', lookup_expr='startswith')
    pizza_name_contains = filters.CharFilter(field_name='pizzas__name', lookup_expr='contains')
    pizza_name_end = filters.CharFilter(field_name='pizzas__name', lookup_expr='endswith')

    order = filters.OrderingFilter(
        fields=PizzaShopSerializer.Meta.fields,
    )

    order_pizzas = filters.OrderingFilter(
        fields=(
            ('pizzas__price', 'price'),
            ('pizzas__size', 'size'),
            ('pizzas__name', 'name'),
        )
    )

    class Meta:
        model = PizzaShopModel
        # якщо хочеш щоб документація/forms бачила поля:
        fields = ['price_lt', 'price_gt', 'price_lte', 'price_gte',
                  'size_lt', 'size_gt', 'size_lte', 'size_gte',
                  'pizza_name_start', 'pizza_name_contains', 'pizza_name_end']
