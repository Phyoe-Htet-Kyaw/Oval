from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db import connections
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.templatetags.static import static
from django.core.files.storage import FileSystemStorage
import random
import math
import os
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

        cursor.execute("SELECT name as username FROM core_userinfo WHERE id= %s", [request.session["user_id"]])
        user_info = cursor.fetchone()

        context = {
            "posts": res,
            "username": user_info[0]
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
            request.session["unregister_username"] = username
            request.session["unregister_email"] = email
            request.session["unregister_password"] = password

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
    del request.session["user_id"]
    return redirect("/login/")


def verify_email_view(request):
    print(request.session["unregister_username"], request.session["unregister_password"])

    digits = [i for i in range(0, 10)]
    random_str = ""

    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])

    print(random_str)
    request.session["verification_code"] = random_str

    template = render_to_string('template/email-template.html', {"code": random_str})
    content = strip_tags(template)
    email = EmailMultiAlternatives(
        'Verification Code',
        content,
        settings.EMAIL_HOST_USER,
        [request.session["unregister_email"]],
    )
    email.attach_alternative(template, "text/html")
    email.fail_silently = False
    email.send()
    return render(request, "auth/verify-email.html")


def checking_verification_code(request):
    response_data = {}
    if request.method == 'POST':
        code = request.POST.get("code", None)

        if code == request.session["verification_code"]:
            del request.session["verification_code"]

            username = request.session["unregister_username"]
            email = request.session["unregister_email"]
            password = request.session["unregister_password"]

            cursor = connections['default'].cursor()
            cursor.execute("INSERT INTO core_userinfo(name, email, password, user_role) VALUES( %s , %s, %s, %s )",
                           [username, email, make_password(password), 0])

            cursor.execute("SELECT id FROM core_userinfo WHERE email= %s ", [email])
            res_id = cursor.fetchone()
            request.session["user_id"] = res_id[0]

            del request.session["unregister_username"]
            del request.session["unregister_email"]
            del request.session["unregister_password"]

            response_data["status"] = 1
            response_data["message"] = "Successful!"
            return JsonResponse(response_data)
        else:
            response_data["status"] = 0
            response_data["message"] = "Your verification code is invalid!"
            return JsonResponse(response_data)
    else:
        response_data["status"] = 0
        response_data["message"] = "Something went wrong!"
        return JsonResponse(response_data)


def upload_profile_picture_view(request):
    return render(request, "auth/upload-profile-picture.html")


def uploading_profile_picture(request):
    profile_pic = request.FILES.get("file", None)
    response_data = {}
    fs = FileSystemStorage()
    fs.save(profile_pic.name, profile_pic)
    url = "C:/Users/pphyo/PycharmProjects/Oval/oval/"
    import base64
    with open(url + "/media/" + profile_pic.name, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())

    cursor = connections['default'].cursor()
    cursor.execute("UPDATE core_userinfo SET profile_picture= %s WHERE id= %s",
                   [my_string, request.session["user_id"]])

    os.remove(url + "/media/" + profile_pic.name)
    response_data["status"] = 1
    response_data["message"] = "Successful!"
    return JsonResponse(response_data)


def upload_cover_photo_view(request):
    return render(request, "auth/upload-cover-photo.html")


def uploading_cover_photo(request):
    cover_photo = request.FILES.get("file", None)
    response_data = {}
    fs = FileSystemStorage()
    fs.save(cover_photo.name, cover_photo)
    url = "C:/Users/pphyo/PycharmProjects/Oval/oval/"
    import base64
    with open(url + "/media/" + cover_photo.name, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())

    cursor = connections['default'].cursor()
    cursor.execute("UPDATE core_userinfo SET cover_photo= %s WHERE id= %s",
                   [my_string, request.session["user_id"]])

    os.remove(url + "/media/" + cover_photo.name)
    response_data["status"] = 1
    response_data["message"] = "Successful!"
    return JsonResponse(response_data)


def testing(request):
    cursor = connections['default'].cursor()
    cursor.execute("SELECT profile_picture FROM core_userinfo WHERE id= %s", [request.session["user_id"]])
    res = cursor.fetchone()
    return render(request, "auth/test.html", {"pro_pic": res[0]})
