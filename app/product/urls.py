from django.contrib import admin
from django.urls import path

from .views import category, search, search_auto, product_detail, add_comment

app_name = 'product'

urlpatterns = [
    path('search/', search, name='search'),
    path('search_auto/', search_auto, name='search_auto'),
    path('addcomment/<product_slug>/', add_comment, name='add_comment'),
    path('<category>/<product>/', product_detail, name='product_detail'),
    path('<category>/', category, name='category'),
]
