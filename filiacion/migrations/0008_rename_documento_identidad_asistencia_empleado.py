# Generated by Django 4.1.5 on 2023-02-10 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0007_remove_empleado_horario_ingreso_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="asistencia",
            old_name="documento_identidad",
            new_name="empleado",
        ),
    ]