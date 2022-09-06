from django.urls import path
from products.views import create_product_sin_alcohol, create_product_con_alcohol, formulario, search_products, bebidas_con_alcohol, bebidas_sin_alcohol, delete_product

urlpatterns = [
    path('create_product_sin_alcohol/', create_product_sin_alcohol, name = 'create_product_sin_alcohol'),
    path('create_product_con_alcohol/', create_product_con_alcohol, name = 'create_product_con_alcohol'),
    path('formulario/', formulario, name= 'formulario'),
    path('search_products/', search_products, name= 'search_products'),
    path('bebidas_con_alcohol/', bebidas_con_alcohol, name = 'bebidas_con_alcohol'),
    path('delete_product/<int:pk>/', delete_product, name = 'delete_product')

]