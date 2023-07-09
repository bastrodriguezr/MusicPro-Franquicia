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
    tipo_instrumento = models.CharField(max_length=50, null=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cantidad)

class CodigoTransporte(models.Model):
    orden_compra = models.IntegerField(default=0)
    codigo_seguimiento = models.CharField(blank=True, max_length=70, verbose_name='Código de seguimiento', null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

class OrdenCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField('Producto', through='ItemOrdenCompra')
    direccion_envio = models.CharField(blank=True, max_length=70, verbose_name='Dirección del pedido', null=True)
    solicitud_exitosa = models.BooleanField(default=False, verbose_name='Solicitud exitosa')
    email = models.EmailField(default='example@example.com')
    
    class Meta:
        verbose_name_plural = "ordenes"

    def __str__(self):
        return f"Orden de compra #{self.id} - Usuario: {self.usuario.username} - Fecha: {self.fecha}"

class ItemOrdenCompra(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    orden_compra = models.ForeignKey('OrdenCompra', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "items"

    def __str__(self):
        return f"Producto: {self.producto.nombre} - Cantidad: {self.cantidad}"
    
class DireccionEnvio(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "direcciones"

    def __str__(self):
        return self.direccion