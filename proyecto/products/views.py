from unicodedata import name
from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Formulario_productos

# Create your views here.

def create_product(request):

    if request.method== 'POST':
        form = Formulario_productos(request.POST)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data ['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                stock = form.cleaned_data['stock']
        )

            return redirect(products_list)

    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'form': form}
        return render(request, 'new_product.html', context=context )

def products_list(request):
    products = Products.objects.all()
    context ={
        'products': products
    }

    return render(request, 'products_list.html', context=context)

def formulario(request):
    print(request.method)
    if request.method== 'POST':
        Products.objects.create(name= request.POST['name'])
    return render(request, 'formulario.html', context={})


def search_products(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)
    context = {
        'products': products
            }
    return render(request, 'search_products.html', context=context)