# Generated by Django 4.1.3 on 2022-11-28 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_proyecto_final', '0007_almacen_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cargo_id',
        ),
        migrations.DeleteModel(
            name='Cargos',
        ),
    ]