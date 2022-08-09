from django.urls import path
from products.views import create_product, products_list, formulario, search_products

urlpatterns = [
    path('create_product/', create_product, name = 'create_product'),
    path('products_list/', products_list, name = 'products_list' ),
    path('formulario/', formulario, name= 'formulario'),
    path('search_products/', search_products, name= 'search_products'),

]