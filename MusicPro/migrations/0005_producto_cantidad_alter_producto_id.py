# Generated by Django 4.2.1 on 2023-05-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0004_alter_producto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
