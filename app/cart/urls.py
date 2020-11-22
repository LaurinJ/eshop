from django.urls import path

from .views import cart_detail, updateItem

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='detail'),
    path('update_item/', updateItem, name='update'),
]
