from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "price", "rating", "sub_category", "is_active"]
    list_display_links = ["title"]
    list_editable = ["rating", "price", "is_active"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)