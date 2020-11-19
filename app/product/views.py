import json

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import Category, Product, Images
from .forms import SearchForm, CommentForm

from ..cart_session.forms import CartForm

def tree_category(cat, parent):
    tree ={}
    for c in cat:
        if c.parent_id == parent:
            tree[c] = [c for c in tree_category(cat, c.id)]
    return tree

def index(request):
    cat = Category.objects.all()
    cart_form = CartForm()
    return render(request, 'index.html', {'category':tree_category(cat, None), 'page':'home', 'cart_form':cart_form})

def category(request, category):
    if category == 'all':
        products = Product.objects.all()
    else:
        cat = Category.objects.get(slug=category)
        products = cat.product_set.all()
    cart_form = CartForm()
    return render(request, 'products.html', {'products':products, 'cart_form':cart_form})

def search(request):
    form = SearchForm(request.GET or None)
    cart_form = CartForm()
    if form.is_valid():
        q = form.cleaned_data['q']
        catid = form.cleaned_data['catid']
        if catid == 0:
            products = Product.objects.filter(title__icontains=q)
        else:
            products = Product.objects.filter(title__icontains=q, category=catid)
        return render(request, 'products.html', {'products':products, 'cart_form':cart_form})
    return HttpResponseRedirect('/')

def product_detail(request, category, product):
    form = CommentForm()
    cart_form = CartForm()
    product = Product.objects.get(slug=product)
    images = Images.objects.filter(product=product)
    return render(request, 'product-page.html', {'product':product, 'images':images, 'form':form, 'cart_form':cart_form})

def add_comment(request, product_slug):
    form = CommentForm(request.POST or None)
    data = {}
    if form.is_valid():
        product = Product.objects.get(slug=product_slug)
        form = form.save(commit=False)
        form.user = request.user
        form.product = product
        form.save()
        data['class'] = 'success'
        data['message'] = 'Komentář byl úspěšně přidán'
        return JsonResponse(data)

    data['class'] = 'error'
    data['message'] = 'Něco se pokazilo zkontroluj formulář'
    return JsonResponse(data)

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for i in product:
            place_json = {}
            place_json = i.title
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

