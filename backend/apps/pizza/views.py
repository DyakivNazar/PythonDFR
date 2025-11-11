from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from .filter import PizzaFilter
from .models import PizzaModel
from .serializer import PizzaPhotoSerializer, PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter


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



