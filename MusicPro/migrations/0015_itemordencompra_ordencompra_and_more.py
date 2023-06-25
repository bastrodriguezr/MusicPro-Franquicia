# Generated by Django 4.2.1 on 2023-06-19 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0014_ordendecompraproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ordendecompraproducto',
            name='orden_de_compra',
        ),
        migrations.RemoveField(
            model_name='ordendecompraproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='OrdenDeCompra',
        ),
        migrations.DeleteModel(
            name='OrdenDeCompraProducto',
        ),
        migrations.AddField(
            model_name='itemordencompra',
            name='orden_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='MusicPro.ordencompra'),
        ),
        migrations.AddField(
            model_name='itemordencompra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicPro.producto'),
        ),
    ]