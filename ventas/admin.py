from django.contrib import admin
# Remove any import of Usuario
from .models import Venta, LineaVenta, Factura, Cliente
# Register your models here.

# Remove this line if it exists:
# admin.site.register(Usuario)

# Keep registration of other models
admin.site.register(Venta)
admin.site.register(LineaVenta)
admin.site.register(Factura)
admin.site.register(Cliente)
