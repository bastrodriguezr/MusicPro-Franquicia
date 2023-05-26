from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('carrito/', views.carrito),
    path('saludo/', views.saludo),
    path('gestionProductos/', views.gestionProductos),
    path('registrarProducto/' , views.registrarProducto),
    path('eliminarProducto/<int:id_producto>/', views.eliminarProducto, name='eliminarProducto'),
]