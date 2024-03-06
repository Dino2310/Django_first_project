from django.shortcuts import render

def sign_in(request):
    return render(request, "users/sign-in.html", {})


def sign_up(request):
    return render(request, "users/sign-in.html", {})


def sign_out(request):
    return render(request, "users/sign-out.html", {})
