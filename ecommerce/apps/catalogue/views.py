from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 21

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get("category_slug"))
        return Product.objects.filter(categories=category)


class ProductSearchView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 21

    def get_queryset(self):
        query = self.request.GET.get('q').lower()
        products = Product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        return products


class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = "product_detail.html"
