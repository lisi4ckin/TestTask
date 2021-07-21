from django.shortcuts import render
from .models import Product, Category


def index(request):
    categories = Category.objects.order_by('-name')
    products = Product.objects.order_by('-name')
    return render(request, 'index.html', {'products': products,
                                          'categories': categories})

