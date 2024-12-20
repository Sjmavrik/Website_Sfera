from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Category, Products


def catalog(request, category_slug):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order = request.GET.get("order", None)

    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if order:
        goods = goods.order_by(order)

    paginator = Paginator(goods, 4)
    current_page = paginator.get_page(page)

    context = {
        "title": "Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {"product": product}

    return render(request, "goods/product.html", context=context)
