from django.urls import path

from carritoApp.views import *
from . import views

urlpatterns = [
    path('', views.home),
    path('carrito/', views.carrito, name="carrito"),
    
    # Carrito
    path('agregar_carrito/<int:producto_id>', agregar_carrito, name='agregar_carrito'),
    path('eliminar_carrito/<int:producto_id>', eliminar_carrito, name='eliminar_carrito'),
    path('restar_carrito/<int:producto_id>', restar_carrito, name='restar_carrito'),
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'),

    path('saludo/', views.saludo),
    path('gestionProductos/', views.gestionProductos, name='gestionProductos'),
    path('registrarProducto/' , views.registrarProducto, name='registrarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    path('enviarCorreo/', views.enviarCorreo, name='enviarCorreo'),
]