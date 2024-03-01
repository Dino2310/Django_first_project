from django.shortcuts import render
from django.http import  HttpResponseNotFound
from .models import Post, Product
from django.contrib.auth.models import User
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

def post_detal(request, slug):
    post =Post.objects.filter(slug=slug)
    if post: return render(request, "app/post.html", { "post" :post[0]} )
    return err(request, 1)


def author_detal(request, at):
    print(f"{at=}")
    author_id = User.objects.get(username = at).id
    print(author_id)
    post = Post.objects.filter(author = author_id)
    print(Post.objects.filter(author = 2)[0].author)
    return render(request, "app/author.html", { "authors" : post} )

def err(request, exception):
    return render(request, '404.html', {})
