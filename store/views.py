from django.shortcuts import render, get_object_or_404
from .models import *
from .utils import min_max_filter

def home(request):
    products = Product.objects.filter().order_by("-rating")[:12]
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


def store(request):
    products = Product.objects.all()
    products = min_max_filter(request, products)

    context = {
        "products": products
    }
    return render(request, "store.html", context)


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)
    products = min_max_filter(request, products)
    
    context = {
        "products": products
    }
    return render(request, "store.html", context) 


def sub_category_products(request, category_slug, sub_category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, slug=sub_category_slug, category=category)
    products = Product.objects.filter(sub_category=subcategory)
    products = min_max_filter(request, products)
    
    context = {
        "products": products
    }
    return render(request, "store.html", context) 


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        "product": product
    }
    return render(request, "product_detail.html", context)