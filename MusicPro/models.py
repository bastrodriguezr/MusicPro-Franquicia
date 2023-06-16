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
    opciones_estado = (
        ('En preparacion', 'En preparacion'),
        ('En camino', 'En camino'),
        ('Completado', 'Completado'),
    )
    opciones_metodo = (
        ('Debito', 'Debito'),
        ('Credito', 'Credito'),
        ('Transferencia', 'Transferencia'),
    )

    codigo_seguimiento = models.AutoField(primary_key=True, unique=True, verbose_name='Codigo de Seguimiento')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de pedido')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha actualizada')
    estado = models.CharField(max_length=20, choices=opciones_estado, default='Pendiente', verbose_name='Estado del Pedido')
    direccion_envio = models.CharField(blank=True, max_length=70, verbose_name='Direccion del pedido')
    metodo_pago = models.CharField(max_length=100, choices=opciones_metodo, blank=True, verbose_name='Metodo de Pago')
    producto = models.ManyToManyField(Producto, blank=True)

    def __str__(self):
        return self.estado