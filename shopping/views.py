from django.shortcuts import redirect, render
from django.urls import reverse

from store.models import Product
from .models import Cart, CartItem, Coupon
from .utils import get_cart

def add_cartitem(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.quantity += 1
    except CartItem.DoesNotExist:
        pass

    cartitem.save()

    return redirect(reverse("cart"))


def subtract_cartitem(request, cartitem_id):

    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        if cartitem.quantity > 1:
            cartitem.quantity -= 1
            cartitem.save()
        else:
            cartitem.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect(reverse("cart"))


def remove_cartitem(request, cartitem_id):

    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect(reverse("cart"))


def cart(request):
    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)
    coupons = ""

    if request.method == "POST":
        coupon = request.POST.get("coupon", None)
        coupons = Coupon.objects.get(code=coupon)
        # cartitems.redused_price = 
        coupons.is_used = True
        coupons.save()
    else:
        coupon=None

    context = {
        "cartitems": cartitems,
        "coupons": coupons
    }
    return render(request, "cart.html", context)

