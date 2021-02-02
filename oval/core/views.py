from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connections

# Create your views here.


def home(request):
    return render(request, "index.html")

# Authentication Pages


def login_form(request):
    return render(request, "auth/login.html")


def register_form(request):
    return render(request, "auth/register.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        con_password = request.POST.get("con_password", None)

        cursor = connections['default'].cursor()
        cursor.execute("INSERT INTO core_userinfo(name, email, password, user_role) VALUES( %s , %s, %s, %s )", [username, email, password, 0])

        status = 1
        return HttpResponse(status)
    else:
        status = 0
        return HttpResponse(status)


def login(request):
    print("GO TO INDEX!")
    return home(request)