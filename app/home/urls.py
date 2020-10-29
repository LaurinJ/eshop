from django.contrib import admin
from django.urls import path

from .views import contact, ContactView

app_name = 'home'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]
