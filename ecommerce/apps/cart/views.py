from django.views.generic import View, DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render

from .models import Cart
from ..catalogue.models import Product


class AddToCart(View):

    def get(self, request, product_id, *args, **kwargs):
        cart_id = request.session.get('cart_id')
        if not cart_id:
            user = request.user
            if request.user.is_authenticated():
                cart = Cart(owner=user, status="open")
            else:
                cart = Cart(status="open")
            cart.save()
        else:
            cart = Cart.objects.get(id=int(cart_id))
        product = Product.objects.get(id=product_id)
        cart.products.add(product)
        # cart.save()
        request.session['cart_id'] = cart.id
        return HttpResponseRedirect(
            reverse('cart:cart_detail', args=(cart.id,))
        )


class RemoveFromCart(View):

    def get(self, request, product_id, *args, **kwargs):
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(id=int(cart_id))
            product = Product.objects.get(id=product_id)
            cart.products.remove(product)
        return HttpResponseRedirect(
            reverse('cart:cart_detail', args=(cart.id,))
        )

class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart.html'


class CheckoutView(LoginRequiredMixin, View):
    # I haven't checked anything for Payment.
    # We can include Payment required later.
    template_name = "checkout_complete.html"

    def get(self, request, cart_id, *args, **kwargs):
        cart = get_object_or_404(Cart, id=int(cart_id))
        if cart.owner and cart.owner != request.user:
            pass
        if not cart.owner:
            cart.owner = request.user
        cart.status = "submitted"
        cart.save()
        del request.session['cart_id']
        return render(request, self.template_name)
