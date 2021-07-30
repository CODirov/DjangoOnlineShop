from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .utils import min_max_filter, get_paginated
from .models import *

def home(request):
    products = Product.objects.filter().order_by("-rating")[:12]
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


def store(request):
    term = request.GET.get("q", None)
    if term:
        products = Product.objects.all().filter(title__contains=term)
        paginated = get_paginated(request, products, 3)

        context = {
            "products" : paginated["items"],
            "pages": paginated["pages"],
            "term": term
        }
        return render(request, "store.html", context)
    else:
        products = Product.objects.all()
        paginated = get_paginated(request, products, 3)

        context = {
            "products" : paginated["items"],
            "pages": paginated["pages"]
        }
        return render(request, "store.html", context)


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)
    products = min_max_filter(request, products)
    
    paginated = get_paginated(request, products, 3)

    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"]
    }

    return render(request, "store.html", context) 


def sub_category_products(request, category_slug, sub_category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_category_slug, category=category)
    products = Product.objects.filter(sub_category=subcategory)
    products = min_max_filter(request, products)
    
    paginated = get_paginated(request, products, 3)

    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"]
    }

    return render(request, "store.html", context) 


def product_detail(request, slug):
    products = Product.objects.filter(slug=slug)
    if not products.exists():
        return render(reverse("home-page"))
    else:
        product = products.first()
    context = {
        "product":product
    }
    return render(request, "product_detail.html", context)