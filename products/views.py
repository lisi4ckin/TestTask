from django.shortcuts import render
from .models import Product, Category
from .forms import SearchForm


def index(request):
    categories = Category.objects.order_by('-name')
    products = Product.objects.order_by('-name')
    form = SearchForm(request.GET)
    FIKER = {
        ('category', 'product_category__name'),
        ('min_price', 'price__gte'),
        ('max_price', 'price__lte'),
    }
    if form.is_valid():
        for k, v in FIKER:
            products = products.filter(**{
                v: form.cleaned_data[k]
            })
    return render(request, 'index.html', {'products': products,
                                         'categories': categories,
                                         'form': form})
