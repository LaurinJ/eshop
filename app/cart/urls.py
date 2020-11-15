from django.contrib import admin
from django.urls import path

from .views import CartDetailView, AddCartView, CartRemoveView, testview, InfoView

app_name = 'cart'

urlpatterns = [
    path('', CartDetailView.as_view(), name='detail'),
    path('add/', AddCartView, name='add'),
    path('remove/<int:product_id>', CartRemoveView.as_view(), name='remove'),
    path('information/', InfoView.as_view(), name='information'),
    path('etest/', testview, name='test123'),
]
