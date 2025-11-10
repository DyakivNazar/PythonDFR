from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.request import Request

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializer import PizzaSerializer
from rest_framework.permissions import IsAdminUser


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.only_capri()
    filterset_class = PizzaFilter
    # permission_classes = (IsAdminUser,)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']
