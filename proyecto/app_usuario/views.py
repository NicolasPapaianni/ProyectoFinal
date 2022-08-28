from django.shortcuts import render, redirect
from app_usuario.forms import Formulario_usuario
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.forms import AuthenticationForm

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

                context = {'message': f' BIenvenido {username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'login.html', {'error': 'El usuario o contraseña ingresado es incorrecto', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# def registro_usuario(request):
#     context = {'form': Formulario_usuario()}
    
#     if request.method == 'POST':
#         form = Formulario_usuario(request.POST)
#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             login(request,user)
        
#         return redirect(registro_usuario)  ## no debería ir a una view en este caso, solo almacenarse en la DB
#                                           ##pero al crear un usuario me arroja error. 
    


#     return render(request, 'registro_usuario.html', context )