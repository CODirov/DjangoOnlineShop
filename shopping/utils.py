from .models import Cart, CartItem


def get_cart(request):
    session_id = request.session.session_key
    if not session_id:
        session_id = request.session.create()
    
    cart = Cart.objects.filter(session_id=session_id)
    if cart.exists():
        cart = cart.first()
    else:
        cart = Cart(session_id=session_id).save()
    
    return cart

    
def get_cartitems_amount(request):
    cart = get_cart(request)
    amount = 0
    if cart:
        cartItems = CartItem.objects.filter(cart=cart)
        for cartItem in cartItems:
            amount+=cartItem.quantity
    return amount


def delete_cart(cart):
    cartitems = CartItem.objects.filter(cart=cart)
    if not cartitems.exists():
        cart.delete()


def get_current_utc():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc)
