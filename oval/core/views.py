from django.shortcuts import render, redirect

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

        print(request.POST.get("email", None))
        return redirect('/')
    else:
        return redirect('register/')


def login(request):
    print("GO TO INDEX!")
    return home(request)