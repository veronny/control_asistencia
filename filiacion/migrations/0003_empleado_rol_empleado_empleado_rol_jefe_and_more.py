# Generated by Django 4.1.5 on 2023-05-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0002_alter_empleado_unidad_organica_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="empleado",
            name="rol_empleado",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="empleado",
            name="rol_jefe",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="empleado",
            name="rol_rrhh",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="empleado",
            name="rol_unidad_organica",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="empleado",
            name="rol_vigilante",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]