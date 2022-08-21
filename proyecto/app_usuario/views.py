from django.shortcuts import render, redirect
from app_usuario.forms import Formulario_usuario
from django.contrib.auth import authenticate, login

# Create your views here.

def registro_usuario(request):
    context = {'form': Formulario_usuario()}
    
    if request.method == 'POST':
        form = Formulario_usuario(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
        
        return redirect(registro_usuario)  ## no debería ir a una view en este caso, solo almacenarse en la DB
                                          ##pero al crear un usuario me arroja error. 
    


    return render(request, 'registro_usuario.html', context )