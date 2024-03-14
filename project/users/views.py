from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *

def sign_in(request):
    form = SignInForm(data = request.POST)
    err = ''   
    if request.method == 'POST':        
        usr_list = User.objects.filter(username = request.POST['username'])
        if usr_list:
            err = "не праильный  пароль"
        else: err = "Нет такого пользователя"
    if form.is_valid():
        user = form.get_user()
        login(request,user)
        return redirect("app:index")
    return render(request, "users/sign-in.html", {'form':form, "err":err})


def sign_up(request):
    reg = SignUpForm(request.POST or None)
    if reg.is_valid() and request.method == 'POST':
        reg.save()
        return redirect('app:index')
    return render(request, "users/sign-up.html", {"reg":reg})


def sign_out(request):
    logout(request)
    return redirect('app:index')
