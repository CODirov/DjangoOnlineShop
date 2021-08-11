from django.contrib import admin

from .models import *



class ProductimageAdmin(admin.StackedInline):
    model = ProductImage
    fields = ["image"]
    extra = 1


class ProductcolorAdmin(admin.StackedInline):
    model = ProductColor
    fields = ["name"]
    extra = 1


class ProductsizeAdmin(admin.StackedInline):
    model = ProductSize
    fields = ["name"]
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "rating", "sub_category", "is_active"]
    list_display_links = ["title"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}

    inlines = [ProductimageAdmin, ProductcolorAdmin, ProductsizeAdmin]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)