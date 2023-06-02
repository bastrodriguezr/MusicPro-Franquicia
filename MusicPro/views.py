from django.shortcuts import render, redirect
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


'''def saludo(request):
    url = 'http://musicpro.bemtorres.win/api/v1/test/saludo'
    try:
        response = requests.get(url)
        data = response.json()
        print(data['message'])
        
    except request.exceptions.RequestException as e:
        print(f'Error: {e}')

    return HttpResponse(data['message'])
'''
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
    

# def registrarProducto(request):
#     nombre = request.POST['txtNombre']
#     precio = request.POST['txtPrecio']
#     descripcion = request.POST['txtDescripcion']
#     imagen = request.FILES['txtImagen']
#     cantidad = request.POST['txtCantidad']

#     producto = Producto.objects.create(nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen, cantidad=cantidad)
#     return redirect('gestionProductos/')

def registrarProducto(request):
    print(request)
    data = {
        # 'nombre': request.POST['txtNombre'],
        # 'precio': request.POST['txtPrecio'],
        # 'descripcion': request.POST['txtDescripcion'],
        # 'imagen': request.FILES['txtImagen'],
        # 'cantidad': request.POST['txtCantidad']
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
    return redirect('gestionProductos')

def error_404(request, exception):
    return render(request, '404.html')
