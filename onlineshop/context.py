from store.models import Category, Subcategory, Product


def categories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated_at")[:6]
    return {
        "categories": categories,
        "subcategories": subcategories,
        "daily_products": daily_products
    }
