from django.shortcuts import render
from .models import Product, Category
from .forms import SearchForm, AddProductForm, AddCategory


def index(request):
    categories = Category.objects.order_by('-name')
    products = Product.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])

        if form.cleaned_data['category']:
            products = products.filter(product_category__name=form.cleaned_data['category'])

        if form.cleaned_data['name']:
            products = products.filter(name__contains=form.cleaned_data['name'])

    if request.user.groups.filter(name='manager').exists():
        return render(request, 'products/products_all.html', {'form': form,
                                                              'products': products})
    if request.user.groups.filter(name='magazine_admin').exists():
        return render(request, 'products/products_all_admin.html', {'form': form,
                                                                    'products': products})
    else:
        return render(request, 'index.html', {'form': form,
                                              'products': products})


def Manager(request):
    form = AddProductForm()
    if request.method == 'POST':
        form = AddProductForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print (form.errors)
    return render(request, 'products/products_add.html', {'form': form})


def Admin(request):
    form = AddCategory()
    if request.method == 'POST':
        form = AddCategory(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print (form.errors)
    return render(request, 'products/category_add.html', {'form': form})
