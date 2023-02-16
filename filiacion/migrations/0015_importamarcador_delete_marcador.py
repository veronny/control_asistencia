# Generated by Django 4.1.5 on 2023-02-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0014_rename_empleado_marcador_dni_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImportaMarcador",
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
                    "Tipo_documento",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "documento_identidad",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "apellido_paterno",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "apellido_materno",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("nombres", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "nombre_completo",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("telefono", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "correo_electronico",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "fecha_nacimiento",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("cargo", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "regimen_laboral",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "fecha_ingreso",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("DNI", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "nombre_completo2",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("fecha", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "horario_ingreso",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "horario_receso",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "horario_reingreso",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "horario_salida",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("Hora_00_06", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_06_07", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_07_08", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_08_09", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_09_10", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_10_11", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_11_12", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_12_13", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_13_14", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_14_15", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_15_16", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_16_17", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_17_18", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_18_19", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_19_20", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_20_21", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_21_22", models.CharField(blank=True, max_length=100, null=True)),
                ("Hora_22_23", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "estado_ingreso",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "estado_salida",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "estado_asistencia",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "hora_ingreso_marcador",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "hora_salida_marcador",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("anio", models.CharField(blank=True, max_length=100, null=True)),
                ("mes", models.CharField(blank=True, max_length=100, null=True)),
                ("dia", models.CharField(blank=True, max_length=100, null=True)),
                ("Duracion", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(name="Marcador",),
    ]