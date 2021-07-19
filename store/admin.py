from django.contrib import admin
from .models import Category, Products, Subcategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'created_at', "updated_at"]
    list_display_links = ["name", 'created_at', "updated_at"]


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'category', 'created_at', "updated_at"]
    list_display_links = ["name", 'category', 'created_at', "updated_at"]


admin.site.register(Subcategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", 'category', "price"]
    list_display_links = ["name", 'category', "price"]
    search_fields = ["name", "price"]

admin.site.register(Products, ProductAdmin)