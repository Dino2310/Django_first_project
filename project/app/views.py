from django.shortcuts import render, redirect
from django.http import  HttpResponseNotFound
from .models import Post, Product, Photo, Comments
from django.contrib.auth.models import User
from .contentTest import abouts, conatact
from .forms import PostForm, ImageForm, CommentForm





def index(request):
    images = Photo.objects.all()
    posts = Post.objects.all()
    return render(request, 'app/index.html', {'posts':posts, "images" : images, "count":1} )

def about (request):
    return render(request, 'app/about.html', abouts)

def contacts(request):
    return render(request, 'app/contacts.html',conatact)

def post_detal(request, slug):
    posts =Post.objects.filter(slug=slug)
    comm = Comments.objects.filter(post__slug = slug)
    if posts:
        if request.method == 'POST':
            answer = CommentForm(request.POST)
            if answer.is_valid():
                instance = answer.save(commit=False)
                instance.user = request.user
                instance.post = posts[0]
                instance.save()
        comment = CommentForm()
        return render(request, "app/post.html", {"post" :posts[0], 'add_comm':comment, "comments": comm})
    return err(request, 1)

def author_detal(request, at):
    post = Post.objects.filter(author__username = at)
    return render(request, "app/author.html", { "authors" : post} )

def comments(request, post):
    list_comm = Comments.objects.filter(post__id = post)
    return render(request, "app/comments.html", {"comments":list_comm})

def err(request, exception):
    return render(request, '404.html', {})


def post_create(request):
    post_form = PostForm(request.POST) 
    print(post_form.errors)
    if request.method == "POST" and post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.author = request.user
        instance.save()
        for image in request.FILES.getlist('images'):
            Photo.objects.create(post=instance, image=image)

        return redirect("app:index")
    post_form = PostForm()
    return render(request, "app/post_create.html", {'post':post_form})

