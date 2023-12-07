from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return HttpResponse('<h1>Bienvenido a BigTimeShop</h1>')

def get_products(request):
    products = Product.objects.all()
    return render(request, 'myApp/productadmin.html', {'products': products})

def delete_product(request):
    return HttpResponse('ahi borramos el producto')