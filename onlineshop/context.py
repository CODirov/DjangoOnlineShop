from store.models import *


def categories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated_at")[:6]
    max_price = Product.objects.filter().order_by("-price").first().price

    return {
        "categories": categories,
        "subcategories": subcategories,
        "daily_products": daily_products,
        "max_price": max_price
    }
