# Generated by Django 4.1.5 on 2023-02-10 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0009_marcador"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marcador",
            name="empleado",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="filiacion.empleado"
            ),
        ),
    ]