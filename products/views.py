from django.shortcuts import render
from products.models import *
from django.db.models import Q


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    related_products = []

    if product.related_product_type == Product.RELATED_PRODUCT_TYPES_MANUAL:
        related_products = product.related_products.all()
    if product.related_product_type == Product.RELATED_PRODUCT_TYPES_PRICE:
        total = product.price
        ten_percent = round(total * 10 / 100)
        related_products = Product.objects.filter(price__range=(product.price - ten_percent, product.price + ten_percent), category_id=product.category.id)
        related_products = related_products.filter(~Q(id=product.id))

    return render(request, 'products/product.html', locals())
