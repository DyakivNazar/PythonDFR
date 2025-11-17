from rest_framework import serializers

from .models import PizzaModel
from ..pizza_shop.models import PizzaShopModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'size', 'price', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     "pizza_shop": {"required": False, "allow_null": True}
        # }


    # def create(self, validated_data):
    #     return PizzaModel.objects.create(**validated_data, pizza_shop_id=1)

    # def validate_price(self, price):
    #     if price <= 0:
    #         raise serializers.ValidationError('Price must be greater than 0')
    #     return price
    #
    # def validate(self, attrs):
    #     price = attrs.get('price')
    #     size = attrs.get('size')
    #
    #     if price == size:
    #         raise serializers.ValidationError('Price cannot be equal to size')
    #
    #     return attrs

class PizzaPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('photo',)


class PizzaResponseSerializer(serializers.Serializer):
    details = serializers.CharField(default='hello')