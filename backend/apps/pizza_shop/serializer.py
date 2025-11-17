from rest_framework import serializers

from ..pizza.serializer import PizzaSerializer
from .models import PizzaShopModel


class PizzaShopSerializer(serializers.ModelSerializer):
    pizzas = serializers.SerializerMethodField()

    class Meta:
        model = PizzaShopModel
        fields = ('id', 'name', 'pizzas')

    def get_pizzas(self, obj):
        # отримаємо request із контексту
        request = self.context.get("request")

        # при POST request = None → повертаємо повний список
        if request is None:
            return PizzaSerializer(obj.pizzas.all(), many=True).data

        params = request.query_params
        qs = obj.pizzas.all()


        price_gt = params.get("price_gt")
        if price_gt is not None:
            qs = qs.filter(price__gt=price_gt)

        price_gte = params.get("price_gte")
        if price_gte is not None:
            qs = qs.filter(price__gte=price_gte)

        price_lt = params.get("price_lt")
        if price_lt is not None:
            qs = qs.filter(price__lt=price_lt)

        price_lte = params.get("price_lte")
        if price_lte is not None:
            qs = qs.filter(price__lte=price_lte)

        size_lt = params.get("size_lt")
        if size_lt is not None:
            qs = qs.filter(size__lt=size_lt)

        size_gt = params.get("size_gt")
        if size_gt is not None:
            qs = qs.filter(size__gt=size_gt)

        size_lte = params.get("size_lte")
        if size_lte is not None:
            qs = qs.filter(size__lte=size_lte)

        size_gte = params.get("size_gte")
        if size_gte is not None:
            qs = qs.filter(size__gte=size_gte)

        name_start = params.get("name_start")
        if name_start is not None:
            qs = qs.filter(name__startswith=name_start)

        name_contains = params.get("name_contains")
        if name_contains is not None:
            qs = qs.filter(name__contains=name_contains)

        name_end = params.get("name_end")
        if name_end is not None:
            qs = qs.filter(name__endswith=name_end)

        pizza_name_start = params.get("pizza_name_start")
        if pizza_name_start is not None:
            qs = qs.filter(name__startswith=pizza_name_start)

        pizza_name_contains = params.get("pizza_name_contains")
        if pizza_name_contains is not None:
            qs = qs.filter(name__contains=pizza_name_contains)

        pizza_name_end = params.get("pizza_name_end")
        if pizza_name_end is not None:
            qs = qs.filter(name__endswith=pizza_name_end)

        order = request.query_params.get("order_pizzas")
        if order:
            qs = qs.order_by(order)

        return PizzaSerializer(qs, many=True).data
