from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная', 
        'content': 'Группа компания СФЕРА'
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас', 
        'content': 'Страница О нас',
        'text_on_page': 'текст о компании'
    }
    
    return render(request, 'main/about.html', context)
