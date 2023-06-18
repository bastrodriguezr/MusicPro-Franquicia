from django.shortcuts import render, HttpResponse, redirect
from .carrito import Carrito
from .context_processor import total_carrito
from MusicPro.models import Producto

def agregar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('carrito')

def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito')

def restar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

def total_compra(request):
    carrito = Carrito(request)
    carrito.calcular_total()
    return redirect('carrito')