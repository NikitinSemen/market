from django.shortcuts import render

from market.models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"products": products, "categories": categories}
    return render(request, "market/index.html", context)


def categories_product(request, categories_id):
    products = Product.objects.filter(Category=categories_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=categories_id)
    context = {
        "products": products,
        "categories": categories,
        "current_category": current_category,
    }
    return render(request, "market/categories_products.html", context)
