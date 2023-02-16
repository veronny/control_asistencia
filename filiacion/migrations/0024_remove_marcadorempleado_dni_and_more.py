# Generated by Django 4.1.5 on 2023-02-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0023_empleado_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="marcadorempleado", name="DNI",),
        migrations.RemoveField(model_name="marcadorempleado", name="duracion",),
        migrations.RemoveField(model_name="marcadorempleado", name="nombre_completo2",),
        migrations.RemoveField(model_name="marcadorempleado", name="user",),
        migrations.AddField(
            model_name="marcadorempleado",
            name="duracion_horas",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="marcadorempleado",
            name="duracion_minutos",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="marcadorempleado",
            name="hora_tolerancia",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="marcadorempleado",
            name="horario_ingreso",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="marcadorempleado",
            name="horario_receso",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="marcadorempleado",
            name="horario_reingreso",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="marcadorempleado",
            name="horario_salida",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="marcadorempleado",
            name="fecha",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
