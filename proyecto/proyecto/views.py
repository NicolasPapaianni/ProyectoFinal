from django.http    import HttpResponse
from django.shortcuts import render


def bienvenida(request):
    return HttpResponse('Bienvenidos a The House of Beer')

def template_home(request):
    return render(request, 'template_home.html', context= {})