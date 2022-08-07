from django.shortcuts import render
from products.models import Products

# Create your views here.

def create_product(request):
    new_product = Products.objects.create(
        name =  'Cerveza',
        price = 150,
        description = 'cerveza negra',
        stock = 50 
        )
    context = {
        'new_product' : new_product
        }
    return render(request, 'new_product.html', context=context )

def products_list(request):
    products = Products.objects.all()
    context ={
        'products': products
    }

    return render(request, 'products_list.html', context=context)