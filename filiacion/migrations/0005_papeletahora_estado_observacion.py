# Generated by Django 4.1.5 on 2023-07-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0004_papeletahora_estado_auditoria_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="papeletahora",
            name="estado_observacion",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
