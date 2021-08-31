from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from store.models import Product
from .models import Cart, CartItem, Coupon
from .utils import get_cart, get_current_utc

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
    context = {}

    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)

    if request.method == "POST":
        coupon_code = request.POST.get("coupon-code", None)
        if coupon_code:
            coupons = Coupon.objects.filter(code=coupon_code)
            if not coupons.exists():
                context["coupon_message"] = "The coupon code doesn't exist."
            else:
                coupon = coupons.first()
                if get_current_utc() > coupon.expires_in:
                    context["coupon_message"] = "The coupon code expired."
                else:
                    for cartitem in cartitems:
                        categories = []
                        for category in coupon.category.all():
                            categories.append(category.name)
                        
                        category = cartitem.product.sub_category.name

                        if category in categories:
                            if cartitem.reduced_price:
                                cartitem.reduced_price = (cartitem.reduced_price * (100 - coupon.stock)) / 100
                            else:
                                cartitem.reduced_price = (cartitem.product.price * (100 - coupon.stock)) / 100
                            cartitem.save()

    context["cartitems"] = cartitems
    
    return render(request, "cart.html", context)


def add_to_cart(request):
    if request.method == "GET":
        try:
            product_id = int(request.GET.get("product_id", None))
            size = int(request.GET.get("size", None))
            color = int(request.GET.get("color", None))
            
            cart = get_cart(request)

            product = Product.objects.get(id=product_id)
            cartitems = CartItem.objects.filter(cart=cart, product=product, color=color, size=size)

            if color == "-1" and size == "-1":
                pass

            elif cartitems.exists():
                cartitem = cartitems.first()
                cartitem.quantity +=1
                cartitem.save()
            
            else:
                cartitem = CartItem(product=product, cart=cart, color=color, size=size)
                cartitem.save()
            
            
            return JsonResponse({"cartitem_count": cartitem.quantity})
            
        except:
            return JsonResponse({"error": "parsing error"})
        
        
    return JsonResponse({"natija": "o'xshadi"})