# Generated by Django 4.2.1 on 2023-06-13 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MusicPro', '0007_alter_transporte_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporte',
            name='usuario',
            field=models.ForeignKey(blank=True, default='auth.User', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
