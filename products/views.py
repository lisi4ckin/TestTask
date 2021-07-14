from django.http import HttpResponse


def index(request):
    return HttpResponse("Main Page")


def about_products(request):
    return HttpResponse("Products")
