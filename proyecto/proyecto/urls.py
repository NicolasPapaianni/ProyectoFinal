
from django.contrib import admin
from django.urls import path, include
from proyecto.views import bienvenida, template_home, template_registrarse, template_contactenos, index 
from app_usuario.views import registro_usuario, login_request, show_profile
from django.contrib.auth.views  import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name = 'bienvenida'),
    path('template_home/', template_home, name = 'template_home' ),
    path('template_registrarse/', template_registrarse, name= 'template_registrarse'),
    path('registro_usuario/', registro_usuario, name ='registro_usuario'),
    path('products/', include('products.urls')),
    path('template_contactenos/', template_contactenos, name = 'template_contactenos' ),
    path('', index, name = 'index'),
    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('perfil/', show_profile, name = 'perfil'),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
