from django.shortcuts import render, HttpResponse, redirect
from .carrito import Carrito
from .context_processor import total_carrito
from MusicPro.models import Producto
from django.contrib import messages
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

def agregar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    if producto.cantidad > 0:
        carrito.agregar(producto)
        producto.cantidad -= 1
        producto.save()
        return redirect('carrito')
    else:
        messages.error(request, 'No hay stock disponible para este producto.')
        return redirect('carrito')
    

def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    cantidad_eliminar = carrito.carrito.get(str(producto_id), {}).get('cantidad', 0)  # Obtener la cantidad del producto en el carrito
    carrito.eliminar(producto)  # Eliminar el producto del carrito
    producto.cantidad += cantidad_eliminar  # Aumentar la cantidad en uno
    producto.save()
    return redirect('carrito')


def restar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    producto.cantidad += 1  # Aumentar la cantidad en uno
    producto.save()
    return redirect('carrito')


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

def total_compra(request):
    carrito = Carrito(request)
    carrito.calcular_total()
    return redirect('carrito')

@receiver(user_logged_out)
def limpiar_carrito_al_cerrar_sesion(sender, request, user, **kwargs):
    carrito = Carrito(request)
    productos_carrito = list(carrito.carrito.values())  # Copia de los elementos del carrito
    carrito.limpiar()  # Vaciar el carrito
    for item in productos_carrito:
        producto_id = item.get('producto_id')
        producto = Producto.objects.get(id=producto_id)
        cantidad_eliminar = item.get('cantidad', 0)
        producto.cantidad += cantidad_eliminar
        producto.save()


