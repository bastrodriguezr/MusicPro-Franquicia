from django.db import models

# Create your models here.

class Producto(models.Model):
    # id = models.AutoField(primary_key=True, unique=True, max_length=6)
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cantidad)