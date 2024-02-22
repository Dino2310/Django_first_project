from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Product


def index(request):
    posts = Post.objects.all()
    prod = Product.objects.all()
    context = {
        'p' : prod,
        'posts':posts,
        'title':'Главная страница',
        'Students': ["Вася", "Петя", "Даня", "Маша"]
        }
    return render(request, 'app/index.html', context )

def about (request):
    context = {
        'title':"Страница о компании"
    }
    return render(request, 'app/about.html',context)

def contacts(request):
    context = {
        'title':'Контакты'
    }
    return render(request, 'app/contacts.html',context)


