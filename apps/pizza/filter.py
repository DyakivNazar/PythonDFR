from django_filters import rest_framework as filters

from apps.pizza.serializer import PizzaSerializer


class PizzaFilter(filters.FilterSet):
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    size_lt = filters.NumberFilter(field_name='size', lookup_expr='lt')
    size_gt = filters.NumberFilter(field_name='size', lookup_expr='gt')
    size_lte = filters.NumberFilter(field_name='size', lookup_expr='lte')
    size_gte = filters.NumberFilter(field_name='size', lookup_expr='gte')
    name_start = filters.CharFilter(field_name='name', lookup_expr='startswith')
    name_contains = filters.CharFilter(field_name='name', lookup_expr='contains')
    name_end = filters.CharFilter(field_name='name', lookup_expr='endswith')

    range = filters.RangeFilter(field_name='size')  # range_min=2&range_max=100
    price_in = filters.BaseInFilter(field_name='price')  # price_in=30,25,2000
    # day = filters.ChoiceFilter('day', choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=PizzaSerializer.Meta.fields
    )  # order=name asc
    # order=-name desc

# PizzaModel.objects.filter(price__gt=0)