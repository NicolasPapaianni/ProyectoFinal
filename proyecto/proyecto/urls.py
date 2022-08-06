
from django.contrib import admin
from django.urls import path
from proyecto.views import bienvenida, template_bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name = 'bienvenida'),
    path('template_bienvenida/', template_bienvenida, name = 'template_bienvenida' )
]
