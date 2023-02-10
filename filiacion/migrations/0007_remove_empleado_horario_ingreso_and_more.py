# Generated by Django 4.1.5 on 2023-02-10 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0006_remove_asistencia_horario_ingreso_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="empleado", name="horario_ingreso",),
        migrations.RemoveField(model_name="empleado", name="horario_receso",),
        migrations.RemoveField(model_name="empleado", name="horario_reingreso",),
        migrations.RemoveField(model_name="empleado", name="horario_salida",),
        migrations.CreateModel(
            name="Tardanza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("tardanza", models.DurationField()),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="filiacion.empleado",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Horario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "horario_ingreso",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "horario_receso",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "horario_reingreso",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "horario_salida",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("hora_entrada", models.TimeField()),
                ("hora_salida", models.TimeField()),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="filiacion.empleado",
                    ),
                ),
            ],
        ),
    ]
