# Generated by Django 4.1.5 on 2023-02-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0032_papeletahora_papeletadia"),
    ]

    operations = [
        migrations.AddField(
            model_name="papeletahora",
            name="lugar_destino",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
