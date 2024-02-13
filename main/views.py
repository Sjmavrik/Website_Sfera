from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category


def index(request):

    categorys = Category.objects.all()

    context = {
        'title': 'Главная', 
        'content': 'Группа компания СФЕРА',
        'categorys': categorys
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас', 
        'content': 'Страница О нас',
        'text_on_page': 'текст о компании'
    }
    
    return render(request, 'main/about.html', context)
