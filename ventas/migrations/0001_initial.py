# Generated by Django 4.2.7 on 2025-03-27 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('telefono_secundario', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('nif', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=10, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, default='España', max_length=100, null=True)),
                ('tipo_cliente', models.CharField(choices=[('particular', 'Particular'), ('empresa', 'Empresa'), ('autonomo', 'Autónomo')], default='particular', max_length=20)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True, verbose_name='Número')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('enviada', 'Enviada'), ('entregada', 'Entregada'), ('cancelada', 'Cancelada')], default='pendiente', max_length=20, verbose_name='Estado')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IVA')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('notas', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente', verbose_name='Cliente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='LineaVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineas', to='ventas.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'Línea de Venta',
                'verbose_name_plural': 'Líneas de Venta',
            },
        ),
        migrations.CreateModel(
            name='HistoricalVenta',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('numero', models.CharField(db_index=True, max_length=20, verbose_name='Número')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('enviada', 'Enviada'), ('entregada', 'Entregada'), ('cancelada', 'Cancelada')], default='pendiente', max_length=20, verbose_name='Estado')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IVA')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('notas', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cliente', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ventas.cliente', verbose_name='Cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'historical Venta',
                'verbose_name_plural': 'historical Ventas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFactura',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('numero', models.CharField(db_index=True, max_length=20, verbose_name='Número de Factura')),
                ('fecha_emision', models.DateField(verbose_name='Fecha de Emisión')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente de pago'), ('pagada', 'Pagada'), ('anulada', 'Anulada')], default='pendiente', max_length=20, verbose_name='Estado')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('venta', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ventas.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'historical Factura',
                'verbose_name_plural': 'historical Facturas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True, verbose_name='Número de Factura')),
                ('fecha_emision', models.DateField(verbose_name='Fecha de Emisión')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente de pago'), ('pagada', 'Pagada'), ('anulada', 'Anulada')], default='pendiente', max_length=20, verbose_name='Estado')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['-fecha_emision'],
            },
        ),
    ]
