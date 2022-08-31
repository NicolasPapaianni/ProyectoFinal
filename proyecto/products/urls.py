from django.urls import path
from products.views import create_product_sin_alcohol, create_product_con_alcohol, formulario, search_products, bebidas_con_alcohol, bebidas_sin_alcohol

urlpatterns = [
    path('create_product_sin_alcohol/', create_product_sin_alcohol, name = 'create_product_sin_alcohol'),
    path('create_product_con_alcohol/', create_product_con_alcohol, name = 'create_product_con_alcohol'),
    # path('products_list/', products_list, name = 'products_list' ),
    path('formulario/', formulario, name= 'formulario'),
    path('search_products/', search_products, name= 'search_products'),
    path('bebidas_con_alcohol/', bebidas_con_alcohol, name = 'bebidas_con_alcohol'),
    path('bebidas_sin_alcohol/', bebidas_sin_alcohol, name = 'bebidas_sin_alcohol')

]