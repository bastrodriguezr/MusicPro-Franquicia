from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('carrito/', views.carrito),
    path('saludo/', views.saludo),
    path('saldo/', views.saldo),
    path('gestionProductos/', views.gestionProductos, name='gestionProductos'),
    path('modificarProductos/', views.modificarProductos, name='modificarProductos'),
    path('registrarProducto/' , views.registrarProducto, name='registrarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    path('editarProducto/<int:id>/', views.editarProducto, name='editarProducto'),
    path('enviarCorreo/', views.enviarCorreo, name='enviarCorreo'),
]