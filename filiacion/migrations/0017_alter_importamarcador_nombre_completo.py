# Generated by Django 4.1.5 on 2023-02-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0016_alter_importamarcador_apellido_materno_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="importamarcador",
            name="nombre_completo",
            field=models.CharField(blank=True, max_length=205, null=True),
        ),
    ]
