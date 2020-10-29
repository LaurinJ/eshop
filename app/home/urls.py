from django.contrib import admin
from django.urls import path

from .views import home, ContactView

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]
