from django.contrib import admin
from .models import UserInfo, University, Country, City, Major, Post, PostType

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'created_at', 'updated_at']
    autocomplete_fields = ['country']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


admin.site.register(UserInfo)
admin.site.register(University)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Post)
admin.site.register(PostType)



