from django.contrib import admin
from .models import Category, Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'created_at', "updated_at"]
    list_display_links = ["name", 'created_at', "updated_at"]


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", 'category', "price"]
    list_display_links = ["name", 'category', "price"]
    search_fields = ["name", "price"]

admin.site.register(Products, ProductAdmin)