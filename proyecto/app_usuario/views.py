from django.shortcuts import render, redirect
from app_usuario.forms import Formulario_usuario
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.views  import LogoutView
from django.http import HttpResponse

# Create your views here.

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                context = {}
                return render(request, 'template_home.html', context = context)

        form = AuthenticationForm()
        return render(request, 'login.html', {'error': 'El usuario o contraseña ingresado es incorrecto', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def registro_usuario(request):
    
    if request.method == 'POST':
        form = Formulario_usuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
            
        else:
            context = {'errors': form.errors}
            form = Formulario_usuario
            context['form'] = form
            return render(request, 'registro_usuario.html', context )

    elif request.method == 'GET':   
        form = Formulario_usuario()
        return render(request, 'registro_usuario.html', {'form': form} )


def show_profile(request):
    if request.user.is_authenticated():

        return HttpResponse(request.user.perfil.first_name)