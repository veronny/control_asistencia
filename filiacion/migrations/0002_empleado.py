# Generated by Django 4.1.5 on 2023-02-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Empleado",
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
                    "tipo_documento",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("DNI", "DNI"),
                            ("Carnet de Extranjeria", "Carnet de Extranjeria"),
                            ("Pasaporte", "Pasaporte"),
                            ("Cedula de Identidad", "Cedula de Identidad"),
                            (
                                "Carnet de solicitante de refugio",
                                "Carnet de solicitante de refugio",
                            ),
                            ("Sin Documento", "Sin Documento"),
                        ],
                        max_length=100,
                        null=True,
                    ),
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
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("nombres", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "nombre_completo",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("telefono", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "correo_electronico",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "perfil",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Consultor", "Consultor"),
                            ("Registrador", "Registrador"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "fecha_nacimiento",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("domicilio", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "genero",
                    models.CharField(
                        blank=True,
                        choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "estado_civil",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Soltero", "Soltero"),
                            ("Casado", "Casado"),
                            ("Viudo", "Viudo"),
                            ("Divorciado", "Divorciado"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "unidad_ejecutora",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "unidad_organica",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "unidad_funcional",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("cargo", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "condicion_laboral",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "regimen_laboral",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "fecha_ingreso",
                    models.CharField(blank=True, max_length=200, null=True),
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
                (
                    "estado",
                    models.CharField(
                        blank=True,
                        choices=[("Activo", "Activo"), ("Inactivo", "Inactivo")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "cuenta_usuario",
                    models.CharField(
                        blank=True,
                        choices=[("Si", "Si"), ("No", "No")],
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
