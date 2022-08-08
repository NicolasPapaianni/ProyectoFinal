from django.http    import HttpResponse
from django.shortcuts import render


def bienvenida(request):
    return HttpResponse('Bienvenidos a The House of Alcohol')

def template_home(request):
    return render(request, 'template_home.html', context= {})

def registrarse(request):
    return HttpResponse('Registrese con nosotros y obtenga sus productos de forma rapida y sencilla')

def template_registrarse(request):
    return render(request, 'template_registrarse.html', context={})