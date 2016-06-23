from django.contrib import admin
from .models import Category, Product, AdditionalImages


class ProductAdmin(admin.ModelAdmin):
    list_filter = (
        ('categories', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ("title", "description", )

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(AdditionalImages)
