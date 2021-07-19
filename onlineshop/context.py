from store.models import Category, Subcategory


def menu(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return {
        "categories": categories,
        "subcategories": subcategories
    }
