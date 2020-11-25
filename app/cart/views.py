from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from app.product.models import Category

from .models import *

def cart_detail(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        print(items)
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}

    return render(request, 'cart/cart_detail.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    else:
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity == 0:
        orderItem.delete()

    return JsonResponse('ok', safe=False)

def address(request):
    return render(request, 'cart/customer_address.html')

def send_method(request):
    delivery = Category.objects.get(slug='zpusob-dopravy')
    method = delivery.product_set.all()
    if request.method == 'POST':
        shipping = request.POST['shipping']
        product = Product.objects.get(id=shipping)

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if method in order.orderitem_set.all():
            pass

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # return redirect("cart:detail")
        print(request.POST['shipping'])
    return render(request, 'cart/pay_delivery_method.html', {'method':method})