from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .filter import PizzaFilter
from .models import PizzaModel
from .serializer import PizzaPhotoSerializer, PizzaSerializer, PizzaResponseSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[],
        operation_description='Hahaha',
        # responses={200: PizzaResponseSerializer()},
        operation_summary='get all piizas'
    )
)
class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = [IsAuthenticatedOrReadOnly]


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']


class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)



