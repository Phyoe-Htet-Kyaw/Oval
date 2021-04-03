"""oval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post_view, name='createPostView'),
    path('upload_post/', views.upload_post, name='uploadPost'),

    path('register/', views.register_form, name="registerForm"),
    path('login/', views.login_form, name="loginForm"),
    path('logout/', views.logout, name="logout"),
    path('registering/', views.register, name="register"),
    path('logining/', views.login, name="login"),
    path('verify_email/', views.verify_email_view, name="verify_email_view"),
    path('verifying/', views.checking_verification_code, name="checking_verification_code"),
    path('upload_profile_picture/', views.upload_profile_picture_view, name="upload_profile_picture_view"),
    path('uploading_profile_picture/', views.uploading_profile_picture, name="uploading_profile_picture"),
    path('upload_cover_photo_view/', views.upload_cover_photo_view, name="upload_cover_photo_view"),
    path('testing/', views.testing, name="testing"),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
