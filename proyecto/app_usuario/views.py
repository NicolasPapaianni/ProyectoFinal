from django.shortcuts import render, redirect
from app_usuario.forms import Formulario_usuario
from django.contrib.auth import authenticate, login

# Create your views here.

def registro_usuario(request):
    context = {
        'form': Formulario_usuario()
    }
    
    if request.method == 'POST':
        form = Formulario_usuario(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
        
        return redirect(to='Home')


    return render(request, 'registro_usuario.html', context )