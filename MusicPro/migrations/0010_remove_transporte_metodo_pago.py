# Generated by Django 4.2.1 on 2023-06-17 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0009_remove_transporte_producto_alter_transporte_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporte',
            name='metodo_pago',
        ),
    ]
