from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('carrito/', views.carrito),
    path('saludo/', views.saludo),
    path('saldo/', views.saldo),
    path('gestionProductos/', views.gestionProductos, name='gestionProductos'),
    path('registrarProducto/' , views.registrarProducto, name='registrarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    path('enviarCorreo/', views.enviarCorreo, name='enviarCorreo'),
]