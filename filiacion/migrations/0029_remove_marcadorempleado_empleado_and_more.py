# Generated by Django 4.1.5 on 2023-02-17 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("filiacion", "0028_remove_empleado_unique_documento_identidad_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="marcadorempleado", name="empleado",),
        migrations.AddField(
            model_name="marcadorempleado",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
