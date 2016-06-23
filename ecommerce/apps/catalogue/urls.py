# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^items/(?P<category_slug>[\w-]+)/$',
        view=views.ProductListView.as_view(),
        name='product_list_category'
    ),

    url(
        regex=r'^search/$',
        view=views.ProductSearchView.as_view(),
        name='search'
    ),

    url(
        regex=r'^(?P<product_slug>[\w-]+)/$',
        view=views.ProductDetailView.as_view(),
        name='product_detail'
    ),
]
