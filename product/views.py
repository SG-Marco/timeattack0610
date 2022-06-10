from unicodedata import category
from django.shortcuts import render

from product.models import CategoryModel, ProductModel

# Create your views here.

def home(request):
    categories = CategoryModel.objects.all()
    return render(request, 'main.html', {'categories': categories})

def show_product(request, id):
    category = CategoryModel.objects.get(id=id)
    products = ProductModel.objects.filter(category=category)
    categories = CategoryModel.objects.all()
    return render(request, 'show_product.html', { 'products': products, 'categories': categories})


def order(request, id):
    product = ProductModel.objects.get(id=id)
    return render(request, 'order.html', {'product': product}) 