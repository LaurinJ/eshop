from django.urls import path

from .views import cart_detail, updateItem, address, send_method

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='detail'),
    path('update_item/', updateItem, name='update'),
    path('address/', address, name='address'),
    path('pay-delivery-method/', send_method, name='method'),
]
