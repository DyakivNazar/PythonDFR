from django_filters import rest_framework as filters

from .models import PizzaShopModel


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

    pizza_name = filters.CharFilter(field_name='pizzas__name', lookup_expr='icontains')

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('name', 'name'),
            ('pizzas__price', 'pizza_price'),
            ('pizzas__size', 'pizza_size'),
        )
    )

    class Meta:
        model = PizzaShopModel
        # якщо хочеш щоб документація/forms бачила поля:
        fields = ['price_lt', 'price_gt', 'price_lte', 'price_gte',
                  'size_lt', 'size_gt', 'size_lte', 'size_gte',
                  'pizza_name']
