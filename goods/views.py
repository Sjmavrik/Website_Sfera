from lib2to3.fixes.fix_input import context
from django.shortcuts import get_object_or_404, render

from goods.models import Products


def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug)) 

    context = {
        'title': 'Каталог',
        'goods': goods,        
    }    
    return render(request, 'goods/catalog.html', context)


def product(request, poduct_slug):

    product = Products.objects.get(slug=poduct_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)