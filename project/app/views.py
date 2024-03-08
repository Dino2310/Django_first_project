from django.shortcuts import render, redirect
from django.http import  HttpResponseNotFound
from .models import Post, Product, Photo
from django.contrib.auth.models import User
from .contentTest import abouts, conatact
from .forms import PostForm, ImageForm





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
    post = Post.objects.filter(author__username = at)
    return render(request, "app/author.html", { "authors" : post} )

def err(request, exception):
    return render(request, '404.html', {})


def post_create(request):
    print(request.__dict__.keys())
    post_form = PostForm(request.POST) 
    if request.method == "POST" and post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.author = request.user
        instance.save()
        for image in request.FILES.getlist('images'):
            Photo.objects.create(post=instance, image=image)

        return redirect("app:index")
    post_form = PostForm()
    return render(request, "app/post_create.html", {'post':post_form})
