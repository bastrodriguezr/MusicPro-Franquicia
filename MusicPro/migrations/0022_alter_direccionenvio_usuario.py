# Generated by Django 4.2.1 on 2023-06-21 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MusicPro', '0021_alter_direccionenvio_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionenvio',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
