# Generated by Django 4.1.5 on 2023-02-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0033_papeletahora_lugar_destino"),
    ]

    operations = [
        migrations.AlterField(
            model_name="papeletahora",
            name="documento_identidad",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
