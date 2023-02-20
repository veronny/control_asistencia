# Generated by Django 4.1.5 on 2023-02-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0036_papeletahora_nombre_completo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="papeletahora",
            name="fecha_papeleta_hora",
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="papeletahora",
            name="hora_retorno",
            field=models.TimeField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="papeletahora",
            name="hora_salida",
            field=models.TimeField(blank=True, max_length=100, null=True),
        ),
    ]
