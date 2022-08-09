from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
# from app_usuario.models import Usuario



class Formulario_usuario(UserCreationForm):             

    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Nombre completo', 
        'last_name': 'Apellido de usuario', 
        'email': 'Direccion de correo',
        'username': 'Nombre de usuario',
        'password1': 'Contraseña', 
        'password2': 'Confirmar contraseña'
        }

