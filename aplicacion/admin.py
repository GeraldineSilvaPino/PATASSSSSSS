from django.contrib import admin

from aplicacion.models import Compra, CompraItem, Producto
# Register your models here.

admin.site.register(Compra)
admin.site.register(CompraItem)

admin.site.register(Producto)




