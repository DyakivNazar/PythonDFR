from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pizza.models import PizzaModel
from pizza.serializers import PizzaSerializer


class PizzaListCreateView(APIView):
    def get(self, *args, **kwargs):
        pizzas = PizzaModel.objects.all()

        serializer = PizzaSerializer(instance=pizzas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PizzaRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response(f'Pizza {pk} does not exist')

        serializer = PizzaSerializer(pizza)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response(f'Pizza {pk} does not exist')

        data = self.request.data
        serializer = PizzaSerializer(instance=pizza, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            PizzaModel.objects.get(pk=pk).delete()
        except PizzaModel.DoesNotExist:
            return Response(f'Pizza {pk} does not exist')

        return Response(status=status.HTTP_204_NO_CONTENT)
