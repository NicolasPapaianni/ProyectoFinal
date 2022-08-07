
from django.contrib import admin
from django.urls import path
from proyecto.views import bienvenida, template_bienvenida
from products.views import create_product, products_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name = 'bienvenida'),
    path('template_bienvenida/', template_bienvenida, name = 'template_bienvenida' ),
    path('create_product/', create_product, name = 'create_product'),
    path('products_list/', products_list, name = 'products_list' )
]
