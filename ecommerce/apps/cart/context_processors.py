from .models import Cart


def cart_processor(request):
    cart_id = request.session.get("cart_id")
    if not cart_id:
        return {}
    cart = Cart.objects.get(id=int(cart_id))
    return {"current_cart": cart}
