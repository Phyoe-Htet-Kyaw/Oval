from django.contrib import admin
from .models import UserInfo, University, Country, City, Major, Post, PostType, AskQuestion, Company

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'created_at', 'updated_at']
    autocomplete_fields = ['country']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


class AskQuestionAdmin(admin.ModelAdmin):
    list_display = ['description', 'user']


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_email', 'created_at', 'updated_at']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_email', 'created_at', 'updated_at']


admin.site.register(UserInfo)
admin.site.register(University, UniversityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Post)
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(AskQuestion, AskQuestionAdmin)



