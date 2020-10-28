from django.contrib import admin
from django.urls import path

from .views import contact

app_name = 'home'

urlpatterns = [
    path('contact/', contact, name='index'),
]
