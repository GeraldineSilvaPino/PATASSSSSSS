# Generated by Django 5.0.6 on 2024-06-28 20:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_producto_remove_compra_fecha_compra_compra_fecha_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='detallecompra',
            name='producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.AddField(
            model_name='producto',
            name='name',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='aplicacion.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
            ],
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='DetalleCompra',
        ),
    ]
