from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from simple_history.models import HistoricalRecords

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('particular', 'Particular'),
        ('empresa', 'Empresa'),
        ('autonomo', 'Autónomo'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    telefono_secundario = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    nif = models.CharField(max_length=20, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, default='España', blank=True, null=True)
    tipo_cliente = models.CharField(max_length=20, choices=TIPO_CHOICES, default='particular')
    sitio_web = models.URLField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)  # Added for soft delete functionality
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Venta(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('enviada', 'Enviada'),
        ('entregada', 'Entregada'),
        ('cancelada', 'Cancelada'),
    ]
    
    numero = models.CharField(max_length=20, unique=True, verbose_name="Número")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    fecha = models.DateField(verbose_name="Fecha")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="IVA")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    history = HistoricalRecords()
    
    def __str__(self):
        return f"Venta {self.numero} - {self.cliente}"
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha']

class LineaVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='lineas', verbose_name="Venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    
    def __str__(self):
        return f"{self.producto.nombre} ({self.cantidad})"
    
    class Meta:
        verbose_name = "Línea de Venta"
        verbose_name_plural = "Líneas de Venta"

class Factura(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente de pago'),
        ('pagada', 'Pagada'),
        ('anulada', 'Anulada'),
    ]
    
    numero = models.CharField(max_length=20, unique=True, verbose_name="Número de Factura")
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Venta")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    history = HistoricalRecords()
    
    def __str__(self):
        return f"Factura {self.numero}"
    
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-fecha_emision']
