
from django.contrib import admin
from django.urls import path
from proyecto.views import bienvenida, template_home
from products.views import create_product, products_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name = 'bienvenida'),
    path('template_home/', template_home, name = 'template_home' ),
    path('create_product/', create_product, name = 'create_product'),
    path('products_list/', products_list, name = 'products_list' )
]
