from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def saludar_a(request):
    return HttpResponse('Hola Django -Hola como estas')

def saludar_a(request, nombre, apellido=''):
    return HttpResponse(f'Hola como estas {nombre.capitalize()} {apellido.capitalize()}')

def mostrar_mi_template(request):
    context={
        'Nombre':'Franco',
        'Apellido':'Goslino',
        'notas': [10, 6, 9, 5],
    }
    return render(request, 'AppCoder/index.html', context=context)
