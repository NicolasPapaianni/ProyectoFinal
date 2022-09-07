from turtle import home
from unicodedata import name
from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Formulario_productos


# Create your views here.

def create_product_sin_alcohol(request):
    if request.user.is_superuser:
        if request.method== 'POST':
            form = Formulario_productos(request.POST, request.FILES)

            if form.is_valid():
                Products.objects.create(
                    name = form.cleaned_data ['name'],
                    price = form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    image = form.cleaned_data['image']
            )

                return redirect(bebidas_sin_alcohol)

        elif request.method == 'GET':
            form = Formulario_productos()
            context = {'form': form}
            return render(request, 'products/new_product.html', context=context )
    
    return redirect('login')

def create_product_con_alcohol(request):
    if request.user.is_superuser:
        if request.method== 'POST':
            form = Formulario_productos(request.POST, request.FILES)

            if form.is_valid():
                Products.objects.create(
                    name = form.cleaned_data ['name'],
                    price = form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    image = form.cleaned_data['image']
            )

                return redirect(bebidas_con_alcohol)

        elif request.method == 'GET':
            form = Formulario_productos()
            context = {'form': form}
            return render(request, 'products/new_product.html', context=context )
    
    return redirect('login')



def formulario(request):
    print(request.method)
    if request.method== 'POST':
        Products.objects.create(name= request.POST['name'])
    return render(request, 'products/formulario.html', context={})


def search_products(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)
    context = {
        'products': products
            }
    return render(request, 'products/search_products.html', context=context)

def bebidas_con_alcohol(request):
    products = Products.objects.all()
    context ={'products': products  }

    return render(request, 'products/bebidas_con_alcohol.html', context=context)


def bebidas_sin_alcohol(request):
    products = Products.objects.all()
    context ={'products': products  }

    return render(request, 'products/bebidas_sin_alcohol.html', context=context)

    

def delete_product(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'products/delete_product.html', context = context)

    if request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(home)


def update_product(request, pk):
    if request.method == 'POST':
        form = Formulario_productos(request.POST)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data ['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.stock = form.cleaned_data['stock']
            product.image = form.cleaned_data['image']
            product.save()

            return redirect(bebidas_con_alcohol)


    elif request.method == 'GET':
        product = Products.objects.get(id=pk)
        form = Formulario_productos(initial= { 'name': product.name, 
                                            'price': product.price, 
                                            'description': product.description,
                                            'stock': product.stock,
                                            'image': product.image}) 
        context = {'form': form}
        return render(request, 'products/update_product.html', context = context )