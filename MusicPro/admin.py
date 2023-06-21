from django.contrib import admin
from .models import Producto, Transporte,ItemOrdenCompra,OrdenCompra,DireccionEnvio

# Register your models here.
admin.site.register(Producto)
admin.site.register(Transporte)
admin.site.register(ItemOrdenCompra)
admin.site.register(OrdenCompra)
admin.site.register(DireccionEnvio)