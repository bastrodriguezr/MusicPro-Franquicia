from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Producto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cantidad)

class Transporte(models.Model):
    codigo_seguimiento = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    codigo_pedido = models.CharField(blank=True, max_length=70, verbose_name='Código de seguimiento')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de pedido')
    direccion_envio = models.CharField(blank=True, max_length=70, verbose_name='Dirección del pedido')

    def __str__(self):
        return self.codigo_pedido