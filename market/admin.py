from django.contrib import admin

from market.models import Product, Category


class MarketAdmin(admin.ModelAdmin):
    list_display = ("Category", "name", "description", "price")
    list_display_links = ("name", "description", "price")
    search_fields = ("name", "description", "price")


admin.site.register(Category)
admin.site.register(Product, MarketAdmin)
