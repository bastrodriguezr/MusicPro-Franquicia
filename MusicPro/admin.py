from django.contrib import admin
from .models import Producto,ItemOrdenCompra,OrdenCompra,DireccionEnvio,CodigoTransporte

# Register your models here.
admin.site.register(Producto)
admin.site.register(CodigoTransporte)
admin.site.register(ItemOrdenCompra)
admin.site.register(OrdenCompra)
admin.site.register(DireccionEnvio)