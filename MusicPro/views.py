from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests

from .models import Producto
from .forms import ProductoForm
from django.contrib import messages

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

def carrito(request):
    return render(request, 'carrito.html')

def saludo(request):
    response = requests.get('https://musicpro.bemtorres.win/api/v1/test/saludo')
    data = response.json()
    return render(request, 'apiSaludo.html', {"message": data['message']})

def saldo(request):
    response = requests.get('https://musicpro.bemtorres.win/api/v1/test/saldo')
    data = response.json()
    return render(request, 'apiSaldo.html', {
        "message": data['message'],
        "saldo": data['saldo'],
        "saldo_raw": data['saldo_raw']
        })

def enviarCorreo(request):
    url = 'http://musicpro.bemtorres.win/api/v1/musicpro/send_email'
    try:
        response = requests.post(url, data={'asunto': 'hola', 'correo': 'ali.munoz@duocuc.cl', 'contenido': ' esto es una prueba de mensaje'})
        data = response.json()
        print(data)
        
    except request.exceptions.RequestException as e:
        print(f'Error: {e}')

    return HttpResponse(data['message'])

def bodega(request):
    response = requests.get('https://musicpro.bemtorres.win/api/v1/bodega/producto')
    data = response.json()
    return render(request, 'apiBodega.html', {
        "productos": data['productos'],
        })

def gestionProductos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
        return render(request, 'gestionProductos.html', {'productos': productos})
    else:
        return render(request, '404.html')
    
def modificarProductos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
        return render(request, 'modificarProductos.html', {'productos': productos})
    else:
        return render(request, '404.html')

def registrarProducto(request):
    print(request)
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect('gestionProductos')
        else:
            messages.error(request, 'Error al agregar el producto')
            data['form'] = formulario
            return render(request, 'gestionProductos.html', data)
    
def eliminarProducto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('gestionProductos')

def error_404(request, exception):
    return render(request, '404.html')

def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto modificado correctamente')
            return redirect('modificarProductos')
        else:
            messages.error(request, 'Error al modificar el producto')
            data['form'] = formulario
            return render(request, 'modificarProductos.html', data)
    return render(request, 'modificarProductos.html', data)


