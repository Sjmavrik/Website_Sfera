from lib2to3.fixes.fix_input import context
from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

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