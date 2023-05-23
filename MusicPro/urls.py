from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('carrito/', views.carrito),
    path('saludo/', views.saludo),
]