from django.contrib import admin
from django.urls import path

from .views import category

app_name = 'product'

urlpatterns = [
    path('<category>/', category, name='category'),
]
