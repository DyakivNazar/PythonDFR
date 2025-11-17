from django.urls import path

from .views import PizzaShopAddPizzaView, PizzaShopListCreateView

urlpatterns=[
    path('', PizzaShopListCreateView.as_view(), name='pizza_shop_list_create'),
    path('/<int:pk>/pizzas', PizzaShopAddPizzaView.as_view(), name='pizza_shop_create_pizza'),
]