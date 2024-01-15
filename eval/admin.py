from django.contrib import admin
from .models import Producto, ProductoVenta, Venta

admin.site.register(Producto)
admin.site.register(ProductoVenta)
admin.site.register(Venta)
