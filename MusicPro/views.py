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

# def registrarProducto(request):
#     nombre = request.POST['txtNombre']
#     precio = request.POST['txtPrecio']
#     descripcion = request.POST['txtDescripcion']
#     imagen = request.FILES['txtImagen']
#     cantidad = request.POST['txtCantidad']

#     producto = Producto.objects.create(nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen, cantidad=cantidad)
#     return redirect('gestionProductos/')

def registrarProducto(request):
    data = {
        'nombre': request.POST['txtNombre'],
        'precio': request.POST['txtPrecio'],
        'descripcion': request.POST['txtDescripcion'],
        'imagen': request.FILES['txtImagen'],
        'cantidad': request.POST['txtCantidad']
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto agregado correctamente')
        else:
            messages.error(request, 'Error al agregar el producto')
            data['form'] = formulario
        return render(request, 'gestionProductos.html', data)
    
def eliminarProducto(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    producto.delete()
    return redirect('gestionProductos/')
