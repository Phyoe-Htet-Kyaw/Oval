from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connections

# Create your views here.


def home(request):
    if "user_id" not in request.session:
        return redirect("/register/")
    else:
        return render(request, "index.html")

# Authentication Pages


def login_form(request):
    return render(request, "auth/login.html")


def register_form(request):
    return render(request, "auth/register.html")


def register(request):
    response_data = {}
    if request.method == 'POST':
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        con_password = request.POST.get("con_password", None)

        cursor = connections['default'].cursor()
        cursor.execute("SELECT COUNT(*) FROM core_userinfo WHERE email= %s ", [email])
        res = cursor.fetchone()

        if res[0] > 0:
            response_data["status"] = 0
            response_data["message"] = "Email already taken! Please try with another email."
            return JsonResponse(response_data)
        else:
            cursor.execute("INSERT INTO core_userinfo(name, email, password, user_role) VALUES( %s , %s, %s, %s )",
                           [username, email, password, 0])

            cursor.execute("SELECT id FROM core_userinfo WHERE email= %s ", [email])
            res_id = cursor.fetchone()
            request.session["user_id"] = res_id[0]

            response_data["status"] = 1
            response_data["message"] = "success"
            return JsonResponse(response_data)
    else:
        response_data["status"] = 0
        response_data["message"] = "Something went wrong!"
        return JsonResponse(response_data)


def login(request):
    print("GO TO INDEX!")
    return home(request)