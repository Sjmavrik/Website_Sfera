from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category


def index(request):

    context = {
        'title': 'Главная', 
        'content': 'Группа компаний СФЕРА', 
    }  
          
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас', 
        'content': 'Страница О нас',
        'text_on_page': 'текст о компании'
    }
    
    return render(request, 'main/about.html', context)


def contact(request):
    context = {
        'title': 'Контакты', 
        'content': 'контакты',
        'text_on_page': 'Контакты компании'
    }
    
    return render(request, 'main/contact.html', context)