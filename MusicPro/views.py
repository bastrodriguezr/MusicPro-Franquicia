from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto, Transporte
from .forms import ProductoForm,TransporteForm
from django.contrib import messages
import requests

#Vista Home
def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

#Vista Carrito
def carrito(request):
    return render(request, 'carrito.html')

#Vista integración Saludo
def saludo(request):
    response = requests.get('https://musicpro.bemtorres.win/api/v1/test/saludo')
    data = response.json()
    return render(request, 'apiSaludo.html', {"message": data['message']})

#Vista integración Saldo
def saldo(request):
    response = requests.get('https://musicpro.bemtorres.win/api/v1/test/saldo')
    data = response.json()
    return render(request, 'apiSaldo.html', {
        "message": data['message'],
        "saldo": data['saldo'],
        "saldo_raw": data['saldo_raw']
        })

#Vista integración Correo
def enviarCorreo(request):
    url = 'http://musicpro.bemtorres.win/api/v1/musicpro/send_email'
    try:
        response = requests.post(url, data={'asunto': 'hola', 'correo': 'ali.munoz@duocuc.cl', 'contenido': ' esto es una prueba de mensaje'})
        data = response.json()
        print(data)
        
    except request.exceptions.RequestException as e:
        print(f'Error: {e}')

    return HttpResponse(data['message'])

#Vista integración Bodega
def bodega(request):
    response = requests.get('https://musicpro.bemtorres.win/api/v1/bodega/producto')
    data = response.json()
    return render(request, 'apiBodega.html', {
        "productos": data['productos'],
        })

#Vista Gestión Productos admin
def gestionProductos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
        return render(request, 'gestionProductos.html', {'productos': productos})
    else:
        return render(request, '404.html')

#Vista agregar nuevo producto
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

#Vista eliminar producto
def eliminarProducto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('gestionProductos')

#Vista Página404
def error_404(request, exception):
    return render(request, '404.html')

#Vista editar productos con modal
def editarProducto(request,id):
    if request.method == "POST":
        imagen = request.FILES.get('imagen')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        producto = Producto(
            id = id,
            imagen = imagen,
            nombre = nombre,
            descripcion = descripcion,
            precio = precio,
            cantidad = cantidad,
        )
        producto.save()
        return redirect('gestionProductos')
    return redirect(request, 'home.html')

#Formulario transporte
def datosTransporte(request):
    data = {
        'form': TransporteForm()
    }
    if request.method == "POST":
        formulario = TransporteForm(data=request.POST)
        direccion_envio = request.POST.get('direccion_envio')
        metodo_pago = request.POST.get('metodo_pago')
        url = 'http://127.0.0.1:7000/api/v1/pedidos/'
        import random
        i = random.randint(1,9999)
        context = {
            'codigo': i, 
        }
        try:
            response = requests.post(url, data={'codigo_seguimiento': i, 
                                                'fecha_creacion': '', 
                                                'fecha_actualizacion': '',
                                                'estado': 'En preparacion',
                                                'direccion_envio': direccion_envio, 
                                                'metodo_pago': metodo_pago, 
                                                'usuario': 21, 
                                                'producto': [1]
                                                })
            data = response.json()
            print(data)  
        except request.exceptions.RequestException as e:
            print(f'Error: {e}')
        if formulario.is_valid():
            formulario.save()
            return render(request, 'envioDatosTransporte.html', context)
        else:
            data["form"] = formulario
    return render(request, 'datosTransporte.html', data)

#Vista Seguimiento
def seguimiento(request):
    return render(request, 'envioDatosTransporte.html')
    
    