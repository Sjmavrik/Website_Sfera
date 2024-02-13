from lib2to3.fixes.fix_input import context
from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Каталог'         
    }    
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render()