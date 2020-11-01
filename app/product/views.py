from django.shortcuts import render

from .models import Category, Product

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
    pruducts = cat.product_set.all()
    return render(request, 'products.html', {'products':pruducts})