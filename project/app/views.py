from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Product
from .contentTest import abouts, conatact


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
    return render(request, 'app/about.html', abouts)

def contacts(request):
    return render(request, 'app/contacts.html',conatact)

