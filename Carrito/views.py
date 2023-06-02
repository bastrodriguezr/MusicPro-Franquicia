from django.shortcuts import render, HttpResponse, redirect

from MusicPro.models import Producto
from .carrito import Carrito
# Create your views here.

def agregar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('/carrito')
