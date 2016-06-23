from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(TimeStampedModel):

    title = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    price = models.FloatField()
    special_price = models.FloatField(null=True)
    base_image = models.ImageField(null=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class AdditionalImages(TimeStampedModel):
    image = models.FileField()
    product = models.ForeignKey(Product, related_name='additional_images')
