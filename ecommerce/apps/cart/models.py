from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

from ..catalogue.models import Product


class Cart(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    status = models.CharField(
        max_length=255,
        choices=(
            ("open", 'open'),
            ("cancelled", 'cancelled'),
            ("submitted", "submitted"),
            ("processed", "processed"),
            ("delivered", "delivered")
        )
    )
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return str(self.pk) + " - " + str(self.owner)

    @property
    def total_price(self):
        total_sum = sum([i.price for i in self.products.all()])
        return total_sum

    @property
    def total_items(self):
        total = len(self.products.all())
        return total
