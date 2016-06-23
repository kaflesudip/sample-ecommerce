# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView

    url(
        regex=r'^(?P<pk>\d+)$',
        view=views.CartDetailView.as_view(),
        name='cart_detail'
    ),

    url(
        regex=r'^add-to-cart/(?P<product_id>\d+)$',
        view=views.AddToCart.as_view(),
        name='add_to_cart'
    ),

    url(
        regex=r'^remove-from-cart/(?P<product_id>\d+)$',
        view=views.RemoveFromCart.as_view(),
        name='remove_from_cart'
    ),

    url(
        regex=r'^checkout/(?P<cart_id>\d+)$',
        view=views.CheckoutView.as_view(),
        name='checkout'
    ),

]
