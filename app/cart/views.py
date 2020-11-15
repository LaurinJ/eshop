from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

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
            return redirect('cart:detail')
    return HttpResponse('Bad')

class CartRemoveView(View):

    def get(self, request, *args, **kwargs):
        self.request.cart.remove(self.kwargs['product_id'])
        return redirect(self.request.META['HTTP_REFERER'])

class InfoView(TemplateView):
    template_name = 'cart/customer_information.html'

def testview(request):
    if request.is_ajax():
        # request.session = request.GET
        print(request.POST)
    data = {'status': 'ok'}
    return JsonResponse(data)