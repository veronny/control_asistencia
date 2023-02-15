import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestante.settings')

from filiacion.models import ImportaMarcador, MarcadorEmpleado

for ImportaMarcador in ImportaMarcador.objects.all():
    MarcadorEmpleado.objects.create(
        DNI = ImportaMarcador.DNI,
        documento_identidad = ImportaMarcador.documento_identidad,
        nombre_completo = ImportaMarcador.nombre_completo,
        nombre_completo2 = ImportaMarcador.nombre_completo2,
        fecha = ImportaMarcador.fecha, 
        hora_ingreso_marcador = ImportaMarcador.hora_ingreso_marcador,
        hora_salida_marcador = ImportaMarcador.hora_salida_marcador, 
        anio = ImportaMarcador.anio,
        mes = ImportaMarcador.mes, 
        dia = ImportaMarcador.dia, 
        Duracion = ImportaMarcador.Duracion,
        user =  ImportaMarcador.DNI  
    )