# Generated by Django 4.2.1 on 2023-06-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0012_ordendecompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='descripcion_pedido',
            field=models.TextField(),
        ),
    ]