from django.urls import path

from apps.pizza_shop.views import PizzaShopListCreateView, PizzaShopAddPizzaView

urlpatterns=[
    path('', PizzaShopListCreateView.as_view()),
    path('/<int:pk>/pizzas', PizzaShopAddPizzaView.as_view()),
]