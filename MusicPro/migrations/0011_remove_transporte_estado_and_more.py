# Generated by Django 4.2.1 on 2023-06-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0010_remove_transporte_metodo_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporte',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='transporte',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='transporte',
            name='usuario',
        ),
        migrations.AddField(
            model_name='transporte',
            name='codigo_pedido',
            field=models.CharField(blank=True, max_length=70, verbose_name='Código de seguimiento'),
        ),
        migrations.AlterField(
            model_name='transporte',
            name='codigo_seguimiento',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='transporte',
            name='direccion_envio',
            field=models.CharField(blank=True, max_length=70, verbose_name='Dirección del pedido'),
        ),
    ]