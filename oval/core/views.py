from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db import connections
from datetime import datetime

# Create your views here.


def home(request):
    if "user_id" not in request.session:
        return redirect("/login/")
    else:
        cursor = connections['default'].cursor()
        cursor.execute("SELECT core_post.id, core_post.description, core_post.post_type_id, core_post.created_at, "
                       "core_userinfo.name FROM `core_post` INNER JOIN core_userinfo ON "
                       "core_post.user_id=core_userinfo.id ORDER BY core_post.id DESC")
        res = cursor.fetchall()
        context = {
            "posts": res
        }
        return render(request, "index.html", context)


def create_post_view(request):
    return render(request, "create-post.html")


def upload_post(request):
    if request.POST.get("post", None) == "":
        return redirect("/create_post/")
    else:
        print(request.POST.get("post", None))
        description = request.POST.get("post", None)
        cursor = connections['default'].cursor()
        cursor.execute("INSERT INTO core_post(description, post_type_id, user_id, university_id, created_at, "
                       "updated_at) VALUES( %s , %s, %s, "
                       "%s, %s, %s )",
                       [description, 1, request.session["user_id"], None, datetime.now(), datetime.now()])
        return redirect("/")


# Authentication Pages


def login_form(request):
    if "user_id" not in request.session:
        return render(request, "auth/login.html")
    else:
        return redirect("/")


def register_form(request):
    if "user_id" not in request.session:
        return render(request, "auth/register.html")
    else:
        return redirect("/")


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
                           [username, email, make_password(password), 0])

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
    response_data = {}
    if request.method == 'POST':
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        cursor = connections['default'].cursor()
        cursor.execute("SELECT COUNT(*) FROM core_userinfo WHERE email= %s ", [email])
        res = cursor.fetchone()

        if res[0] > 0:

            cursor.execute("SELECT * FROM core_userinfo WHERE email= %s ", [email])
            res_user = cursor.fetchone()

            if res_user[4] == email:
                if check_password(password, res_user[5]):
                    request.session["user_id"] = res_user[0]
                    response_data["status"] = 1
                    response_data["message"] = "success"
                    return JsonResponse(response_data)
                else:
                    response_data["status"] = 0
                    response_data["message"] = "Your password was invalid!."
                    return JsonResponse(response_data)
            else:
                response_data["status"] = 0
                response_data["message"] = "Your email was invalid!."
                return JsonResponse(response_data)
        else:
            response_data["status"] = 0
            response_data["message"] = "Your email was not found!."
            return JsonResponse(response_data)

    else:
        response_data["status"] = 0
        response_data["message"] = "Something went wrong!"
        return JsonResponse(response_data)


def logout(request):
    print("LOGOUT")
    del request.session["user_id"]
    return redirect("/login/")