from django.urls import path

from carritoApp.views import *
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('carrito/', views.carrito, name="carrito"),
    path('confirmar/', views.confirmarCompra, name="confirmar-compra"),
    path('realizada/', views.compraRealizada, name="compra-realizada"),
    path('pago/', views.realizar_pago, name="realizar-pago"),
    path('pago/realizado/', views.pago_realizado, name="pago-realizado"),

    # Carrito
    path('agregar_carrito/<int:producto_id>', agregar_carrito, name='agregar_carrito'),
    path('eliminar_carrito/<int:producto_id>', eliminar_carrito, name='eliminar_carrito'),
    path('restar_carrito/<int:producto_id>', restar_carrito, name='restar_carrito'),
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'),

    # Integraciones
    path('saludo/', views.saludo),
    path('saldo/', views.saldo),
    path('bodega/', views.bodega),
    path('enviarCorreo/', views.enviarCorreo, name='enviarCorreo'),
    path('transporte/', views.transporte, name='transporte'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),

    #WebPay
    path('pago_webpay/', views.realizar_pago_webpay, name="realizar-pago-webpay"),
    path('pago/realizado_webpay/', views.pago_realizado_webpay, name="pago-realizado-webpay"),

    # CRUD
    path('gestionProductos/', views.gestionProductos, name='gestionProductos'),
    path('registrarProducto/' , views.registrarProducto, name='registrarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    path('editarProducto/<int:id>/', views.editarProducto, name='editarProducto'),
]