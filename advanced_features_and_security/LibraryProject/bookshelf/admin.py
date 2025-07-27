from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.urls import path, include
from .models import Book, CustomUser

# Register your models here.

class ModelAdmin(UserAdmin):
    pass
    # list_display = ("title", "author", "publication_year",)
    # list_filter = ("title", "author", "publication_year",)
    # search_fields = ("title", "author",)


admin.site.register(CustomUser, ModelAdmin)
