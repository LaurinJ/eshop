import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Category, Product, Images
from .forms import SearchForm

def tree_category(cat, parent):
    tree ={}
    for c in cat:
        if c.parent_id == parent:
            tree[c] = [c for c in tree_category(cat, c.id)]
    return tree

def index(request):
    cat = Category.objects.all()
    return render(request, 'index.html', {'category':tree_category(cat, None), 'page':'home'})

def category(request, category):
    cat = Category.objects.get(slug=category)
    products = cat.product_set.all()
    return render(request, 'products.html', {'products':products})

def search(request):
    form = SearchForm(request.GET or None)
    if form.is_valid():
        q = form.cleaned_data['q']
        catid = form.cleaned_data['catid']
        if catid == 0:
            products = Product.objects.filter(title__icontains=q)
        else:
            products = Product.objects.filter(title__icontains=q, category=catid)
        return render(request, 'products.html', {'products':products})
    return HttpResponseRedirect('/')

def product_detail(request, category, product):
    product = Product.objects.get(slug=product)
    images = Images.objects.filter(product=product)
    return render(request, 'product-page.html', {'product':product, 'images':images})

def search_auto(request):
    if request.is_ajax():
        print('ok')
        q = request.GET.get('term', '')
        print(q)
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

