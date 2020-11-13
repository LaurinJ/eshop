from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .cart import Cart
from .forms import CartForm

class CartDetailView(TemplateView):
    template_name = 'cart/cart_detail.html'

def AddCartView(request):
    form = CartForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cart = Cart(request.session)
            cart.add(**form.cleaned_data)
            print(cart.cart)
            return HttpResponse('ok')
    return HttpResponse('Bad')