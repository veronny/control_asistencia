# Generated by Django 4.1.5 on 2023-02-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0003_empleado_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="cargo",
            field=models.CharField(
                blank=True,
                choices=[
                    ("DIRECTOR/A GENERAL", "DIRECTOR/A GENERAL"),
                    ("DIRECTOR/A EJECUTIVO/A", "DIRECTOR/A GENERAL"),
                    ("DIRECTOR EJEC. ADJUNTO", "DIRECTOR EJEC. ADJUNTO"),
                    ("DIRECTOR SIST.ADM.I", "DIRECTOR SIST.ADM.I"),
                    ("MEDICO", "MEDICO"),
                    ("MEDICO I", "MEDICO I"),
                    ("MEDICO IV", "MEDICO IV"),
                    ("MEDICO ESPECIALISTA", "MEDICO ESPECIALISTA"),
                    ("ASIST. SOCIAL", "ASIST. SOCIAL"),
                    ("BIOLOGO", "BIOLOGO"),
                    ("BIOLOGO I", "BIOLOGO I"),
                    ("CIRUJANO DENTISTA", "CIRUJANO DENTISTA"),
                    ("ENFERMERA/O", "ENFERMERA/O"),
                    ("MEDICO VETERINARIO", "MEDICO VETERINARIO"),
                    ("NUTRICIONISTA", "NUTRICIONISTA"),
                    ("OBSTETRA", "OBSTETRA"),
                    ("PSICOLOGO", "PSICOLOGO"),
                    ("PSICOLOGO IV", "PSICOLOGO IV"),
                    ("QUIMICO FARMACEUTICO", "QUIMICO FARMACEUTICO"),
                    ("TECNOLOGO MEDICO", "TECNOLOGO MEDICO"),
                    ("ABOGADO I", "ABOGADO I"),
                    ("ABOGADO II", "ABOGADO II"),
                    ("ARQUITECTO IV", "ARQUITECTO IV"),
                    ("ASIST. ADMINIST. II", "ASIST. ADMINIST. II"),
                    ("ESP. ADMINIST. I", "ESP. ADMINIST. I"),
                    ("ESP. ADMINIST. II", "ESP. ADMINIST. II"),
                    ("ESP. ADMINIST. III", "ESP. ADMINIST. III"),
                    ("ESP. EN RACIONALIZ. II", "ESP. EN RACIONALIZ. II"),
                    ("ESTADISTICO II", "ESTADISTICO II"),
                    ("INGENIERO I", "INGENIERO I"),
                    ("INGENIERO II", "INGENIERO II"),
                    ("ARTESANO IV", "ARTESANO IV"),
                    ("CAJERO/A II", "CAJERO/A II"),
                    ("OPERAD. EQUIPO ELEC. II", "OPERAD. EQUIPO ELEC. II"),
                    ("OPERADOR P.A.D. I", "OPERADOR P.A.D. I"),
                    ("SECRETARIA III", "SECRETARIA III"),
                    ("SECRETARIA V", "SECRETARIA V"),
                    ("TEC. EN ABOGACIA II", "TEC. EN ABOGACIA II"),
                    ("TEC. EN ARCHIVO III", "TEC. EN ARCHIVO III"),
                    ("TEC. EN ENFERMERIA", "TEC. EN ENFERMERIA"),
                    ("TEC. EN ENFERMERIA I", "TEC. EN ENFERMERIA I"),
                    ("TEC. EN FARMACIA I", "TEC. EN FARMACIA I"),
                    ("TEC. EN TRANSPORTE II", "TEC. EN TRANSPORTE II"),
                    ("TEC. SANITARIO I", "TEC. SANITARIO I"),
                    ("ESP. EN SALUD OCUP. I", "ESP. EN SALUD OCUP. I"),
                    ("TECNICO/A ADMINIST. I", "TECNICO/A ADMINIST. I"),
                    ("TECNICO/A ADMINIST. II", "TECNICO/A ADMINIST. II"),
                    ("TECNICO/A ADMINIST. III", "TECNICO/A ADMINIST. III"),
                ],
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="condicion_laboral",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Nombrado", "Nombrado"),
                    ("Contrato Plazo Fijo", "Contrato Plazo Fijo"),
                    ("Contrato Plazo Indet.", "Contrato Plazo Indet."),
                    ("Contrato-CAS", "Contrato-CAS"),
                    ("Destacado Externo", "Destacado Externo"),
                    ("CONTRAT. P.S./CAS ASISTENCIAL", "CONTRAT. P.S./CAS ASISTENCIAL"),
                ],
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="perfil",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Administrador", "Administrador"),
                    ("Registrador", "Registrador"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="regimen_laboral",
            field=models.CharField(
                blank=True,
                choices=[
                    ("D.L. 1057-D.Leg 1057", "D.L. 1057-D.Leg 1057"),
                    ("Nombrado", "Nombrado"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
