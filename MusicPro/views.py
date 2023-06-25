from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from carritoApp.carrito import Carrito
from .models import Producto,ItemOrdenCompra, OrdenCompra,DireccionEnvio,CodigoTransporte
from .forms import ProductoForm,DireccionEnvioForm
from django.contrib import messages
import requests, json, datetime
from django.core.mail import send_mail
from django.conf import settings

#Vista Home
def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

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
    url = 'https://musicpro.bemtorres.win/api/v1/musicpro/send_email'
    try:
        response = requests.post(url, data={'asunto': 'hola', 'correo': 'ba.prado@duocuc.cl', 'contenido': ' esto es una prueba de mensaje'})
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
'''def datosTransporte(request):
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
    return render(request, 'datosTransporte.html', data)'''

'''def datosTransporte(request):
    data = {
        'form': TransporteForm()
    }
    if request.method == "POST":
        formulario = TransporteForm(data=request.POST)
        direccion_envio = request.POST.get('direccion_envio')
        url = 'https://musicpro.bemtorres.win/api/v1/transporte/solicitud'
        try:
            response = requests.post(url, data={'nombre_origen': request.user.username, 
                                                'direccion_origen': 'Av. Crimson 4245', 
                                                'nombre_destino': 'Patrick Star',
                                                'estado': 'En preparacion',
                                                'direccion_destino': direccion_envio, 
                                                'comentario': 'Primer intento', 
                                                'info': 'Carga con instrumentos pesados'
                                                })
            data = response.json()
            print(data)  
        except request.exceptions.RequestException as e:
            print(f'Error: {e}')
        if formulario.is_valid():
                formulario.save()
                # Vaciar el carrito después de realizar el pago
                carrito = Carrito(request)
                carrito.limpiar()
                return render(request, 'envioDatosTransporte.html', {'data': data})
        else:
            data["form"] = formulario
    return render(request, 'datosTransporte.html', data)'''

#Vista Carrito
def carrito(request):

    #Generar carrito
    carrito = Carrito(request)
    total = carrito.calcular_total()
    carrito_items = carrito.carrito.values()
    context = {
        'total': total,
        'carrito_items': carrito_items
    }
    return render(request, 'carrito.html', context)

#Vista Confirmar compra V2 (para actualizar o crear nuve direccion)
def confirmarCompra(request):
    # Generar carrito
    carrito = Carrito(request)
    total = carrito.calcular_total()
    carrito_items = carrito.carrito.values()
    direcciones = DireccionEnvio.objects.all()

    data = {
        'form': DireccionEnvioForm(),
        'total': total,
        'carrito_items': carrito_items,
        'direcciones': direcciones
    }

    if request.method == 'POST':
        formulario = DireccionEnvioForm(request.POST)
        if formulario.is_valid():
            direccion = formulario.cleaned_data['direccion']
            # Obtener la dirección existente del usuario (si la hay)
            direccion_envio = DireccionEnvio.objects.filter(usuario=request.user).first()
            if direccion_envio:
                # Actualizar la dirección existente
                direccion_envio.direccion = direccion
                direccion_envio.save()
            else:
                # Crear una nueva dirección
                DireccionEnvio.objects.create(usuario=request.user, direccion=direccion)
    else:
        formulario = DireccionEnvioForm()
        data['form'] = formulario

    return render(request, 'confirmarCompra.html', data)
    
    
#Vista Compra realizada
def compraRealizada(request):

    #Generar carrito
    carrito = Carrito(request)
    total = carrito.calcular_total()
    carrito_items = carrito.carrito.values()

    context = {
        'total': total,
        'carrito_items': carrito_items
    }
    
    direccion_envio = DireccionEnvio.objects.get(usuario=request.user)

    # Guardar la orden de compra
    if request.method == 'POST':
        usuario = request.user if request.user.is_authenticated else None
        if usuario:
            total_cantidad = 0
            orden_compra = OrdenCompra.objects.create(usuario=usuario,direccion_envio=direccion_envio.direccion,email=request.user.email)
            for item in carrito_items:
                producto = Producto.objects.get(id=item['producto_id'])
                ItemOrdenCompra.objects.create(
                        producto=producto,
                        orden_compra=orden_compra,
                        cantidad=item['cantidad']
                    )
            orden_compra.save()
            total_cantidad += item['cantidad']
            context = {
                'orden_compra': orden_compra,
                'producto': producto,
                'total_cantidad': total_cantidad,
                'total': total,
                'carrito_items': carrito_items
            }
            carrito.limpiar()
            return render(request, 'compraRealizada.html',context)
        else:
            # Manejar el caso en el que el usuario no esté autenticado
            return redirect('login')

#Vista transporte(Admin) 
def transporte(request):
    if request.user.is_superuser:
        ordenes = OrdenCompra.objects.all()
        items = ItemOrdenCompra.objects.all()
        
        context = {
            'ordenes': ordenes,
            'items':items,
            }
        
        if request.method == "POST":
            orden_id = request.POST.get("orden_id")
            opcion = request.POST.get('opcion')
            print(orden_id)
            orden= get_object_or_404(OrdenCompra, id=orden_id)
            now = datetime.datetime.now()
            fecha_pedido = now.isoformat()

            if opcion == 'GranJVCorp':
                data = {
                    "direccion_origen": "Av. Kennedy 8745",
                    "nombre_destino": orden.usuario.username,
                    "direccion_destino": orden.direccion_envio,
                    "correo_destino": orden.email,
                    "estado": "En preparacion",
                    "fecha_pedido": fecha_pedido
                }
                url = 'http://127.0.0.1:7000/pedidos/api/v1/pedidos/'
                
                try:
                    response = requests.post(url, json=data)
                    response.raise_for_status() 
                    response_data = response.json()
                    print(response_data)
                    orden.solicitud_exitosa = True
                    orden.save()
                    # Acceder a los datos de respuesta
                    codigo_seguimiento = response_data['codigo_seguimiento']
                    CodigoTransporte.objects.create(
                        orden_compra=orden_id,
                        codigo_seguimiento=codigo_seguimiento,
                        usuario=orden.usuario
                    )
                    subject = 'Código de seguimiento'
                    message = f'Gracias por comprar en Music Pro, tu codigo de seguimiento es: #{codigo_seguimiento}'
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [orden.email]
                    send_mail(subject, message, from_email, recipient_list)
                    messages.success(request, 'Solicitud enviada correctamente')
                    return redirect('home')
                except requests.exceptions.RequestException as e:
                    print(f'Error en la solicitud: {e}')
            elif opcion == 'MusicPro':
                data={
                    'nombre_origen': request.user.username, 
                    'direccion_origen': 'Av. Kennedy 8745', 
                    'nombre_destino': orden.usuario.username,
                    'estado': 'En preparacion',
                    'direccion_destino': orden.direccion_envio, 
                    'comentario': 'Primer intento', 
                    'info': 'Carga con instrumentos pesados'
                }
                url = 'https://musicpro.bemtorres.win/api/v1/transporte/solicitud'
                
                try:
                    response = requests.post(url, json=data)
                    response.raise_for_status() 
                    response_data = response.json()
                    print(response_data)
                    orden.solicitud_exitosa = True
                    orden.save()
                    # Acceder a los datos de respuesta
                    codigo_seguimiento = response_data['codigo_seguimiento']
                    CodigoTransporte.objects.create(
                        orden_compra=orden_id,
                        codigo_seguimiento=codigo_seguimiento,
                        usuario=orden.usuario
                    )
                    subject = 'Código de seguimiento'
                    message = f'Gracias por comprar en Music Pro, tu codigo de seguimiento es: #{codigo_seguimiento}'
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [orden.email]
                    send_mail(subject, message, from_email, recipient_list)
                    messages.success(request, 'Solicitud enviada correctamente')
                    return redirect('home')
                except requests.exceptions.RequestException as e:
                    print(f'Error en la solicitud: {e}')
    else:
        return render(request, '404.html')
    return render(request, 'transporte.html', context)

#Vista Seguimiento
def seguimiento(request):
    codigo_seguimiento = ""
    verificacion = ""
    if request.method == "POST":
        codigo_seguimiento = request.POST.get("codigo_seguimiento")
    primeros_dos_caracteres = codigo_seguimiento[:2]
    if primeros_dos_caracteres == 'JV':
        try:
            response = requests.get(f'http://127.0.0.1:7000/pedidos/estado/{codigo_seguimiento}')
            data = response.json()
            verificacion = "JV"
            return render(request, 'seguimiento.html', {
                "estado": data['estado'],
                "direccion_origen": data['direccion_origen'],
                "direccion_destino": data['direccion_destino'],
                "verificacion": verificacion
            })
        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud: {e}')
            mensaje_error = 'Error en la solicitud. Por favor, intenta nuevamente más tarde.'
            return render(request, 'seguimiento.html', {'error': mensaje_error})
    else:
        try:
            response = requests.get(f'https://musicpro.bemtorres.win/api/v1/transporte/seguimiento/{codigo_seguimiento}')
            data = response.json()
            result = data.get('result', {})
            solicitud = result.get('solicitud', {})
            verificacion = "MP" 
            return render(request, 'seguimiento.html', {
                "status": data['status'],
                "result": result,
                "solicitud": solicitud,
                "verificacion": verificacion
            })
        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud: {e}')
            mensaje_error = 'Error en la solicitud. Por favor, intenta nuevamente más tarde.'
            return render(request, 'seguimiento.html', {'error': mensaje_error})

