from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def products(request):
    products = Product.objects.order_by('-name')[:1]
    return render(request, 'products/products.html', {'products': products})
