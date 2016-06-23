from django.contrib import admin
from .models import Cart


class ChoicesFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ("open", 'open'),
            ("cancelled", 'cancelled'),
            ("submitted", "submitted"),
            ("processed", "processed"),
            ("delivered", "delivered")
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        else:
            return queryset


class CartAdmin(admin.ModelAdmin):
    list_filter = (ChoicesFilter,)

admin.site.register(Cart, CartAdmin)
