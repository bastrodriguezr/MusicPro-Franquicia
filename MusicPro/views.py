from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Producto

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

def carrito(request):
    return render(request, 'carrito.html')


def saludo(request):
    url = 'http://musicpro.bemtorres.win/api/v1/test/saldo'
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        
    except request.exceptions.RequestException as e:
        print(f'Error: {e}')

    return HttpResponse(data['message'])

def gestionProductos(request):
    productos = Producto.objects.all()
    return render(request, 'gestionProductos.html', {'productos': productos})
