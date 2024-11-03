from unicodedata import category

from django.urls import path

from market.apps import MarketConfig
from market.views import index, categories_product

app_name = MarketConfig.name

urlpatterns = [
    path("", index, name="products"),
    path("<int:categories_id>/", categories_product, name="categories_product"),
]
