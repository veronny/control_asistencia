# Generated by Django 4.1.5 on 2023-02-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0024_remove_marcadorempleado_dni_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="marcadorempleado",
            name="fecha_marcacion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
