from django.db import models
from django.contrib.auth.models import User
class Red(models.Model):
    nombre_red = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="", null=True, blank=True)
    def __str__(self):
        return self.nombre_red
class Microred(models.Model):
    nombre_microred = models.CharField(max_length=100,null=True, blank=True)
    cod_mic = models.CharField(max_length=10, default="",null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="",null=True, blank=True)
    red = models.ForeignKey(Red, on_delete=models.CASCADE, related_name='redes',null=True, blank=True)  
    def __str__(self):
        return self.nombre_microred   
class Establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=100, null=True, blank=True)
    codigo_unico = models.CharField(max_length=100, default="", null=True, blank=True)
    red = models.ForeignKey(Red, on_delete=models.CASCADE, null=True, blank=True)
    microred = models.ForeignKey(Microred, on_delete=models.CASCADE, related_name='microredes', null=True, blank=True)  
    def __str__(self):
        return self.nombre_establecimiento     
class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=100,null=True, blank=True)
    ubigeo = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nombre_provincia        
class Distrito(models.Model):
    nombre_distrito = models.CharField(max_length=100, null=True, blank=True)
    ubigeo = models.CharField(max_length=100, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='provincias', null=True, blank=True)  
    def __str__(self):
        return self.nombre_distrito
# Create your models here.
class Filiacion(models.Model):
    TIPO_MUNICIPALIDAD = [
                ('Provincial', 'Provincial'),
                ('Distrital', 'Distrital'),
            ]
    
    PERFIL = [
                ('Administrador', 'Administrador'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    provincia = models.CharField(max_length=100,null=True, blank=True)
    distrito = models.CharField(max_length=100,null=True, blank=True)
    tipo_municipalidad = models.CharField(choices=TIPO_MUNICIPALIDAD, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
class Empleado(models.Model):
    TIPO_DOCUMENTO = [
                ('DNI', 'DNI'),
                ('Carnet de Extranjeria', 'Carnet de Extranjeria'),
                ('Pasaporte', 'Pasaporte'),
                ('Cedula de Identidad', 'Cedula de Identidad'),
                ('Carnet de solicitante de refugio', 'Carnet de solicitante de refugio'),
                ('Sin Documento', 'Sin Documento'),
            ]
    
    PERFIL = [
                ('Administrador', 'Administrador'),
                ('Registrador', 'Registrador'),
            ]
    
    GENERO = [
                ('Masculino', 'Masculino'),
                ('Femenino', 'Femenino'),
            ]
    
    ESTADO_CIVIL = [
                ('Soltero', 'Soltero'),
                ('Casado', 'Casado'),
                ('Viudo', 'Viudo'),
                ('Divorciado', 'Divorciado'),
            ]
    
    CARGO = [
                ('DIRECTOR/A GENERAL','DIRECTOR/A GENERAL'),
                ('DIRECTOR/A EJECUTIVO/A','DIRECTOR/A GENERAL'),
                ('DIRECTOR EJEC. ADJUNTO','DIRECTOR EJEC. ADJUNTO'),
                ('DIRECTOR SIST.ADM.I','DIRECTOR SIST.ADM.I'),
                ('MEDICO','MEDICO'),
                ('MEDICO I','MEDICO I'),
                ('MEDICO IV','MEDICO IV'),
                ('MEDICO ESPECIALISTA','MEDICO ESPECIALISTA'),
                ('ASIST. SOCIAL','ASIST. SOCIAL'),
                ('BIOLOGO','BIOLOGO'),
                ('BIOLOGO I','BIOLOGO I'),
                ('CIRUJANO DENTISTA','CIRUJANO DENTISTA'),
                ('ENFERMERA/O','ENFERMERA/O'),
                ('MEDICO VETERINARIO','MEDICO VETERINARIO'),
                ('NUTRICIONISTA','NUTRICIONISTA'),
                ('OBSTETRA','OBSTETRA'),
                ('PSICOLOGO','PSICOLOGO'),
                ('PSICOLOGO IV','PSICOLOGO IV'),
                ('QUIMICO FARMACEUTICO','QUIMICO FARMACEUTICO'),
                ('TECNOLOGO MEDICO','TECNOLOGO MEDICO'),
                ('ABOGADO I','ABOGADO I'),
                ('ABOGADO II','ABOGADO II'),
                ('ARQUITECTO IV','ARQUITECTO IV'),
                ('ASIST. ADMINIST. II','ASIST. ADMINIST. II'),
                ('ESP. ADMINIST. I','ESP. ADMINIST. I'),
                ('ESP. ADMINIST. II','ESP. ADMINIST. II'),
                ('ESP. ADMINIST. III','ESP. ADMINIST. III'),
                ('ESP. EN RACIONALIZ. II','ESP. EN RACIONALIZ. II'),
                ('ESTADISTICO II','ESTADISTICO II'),
                ('INGENIERO I','INGENIERO I'),
                ('INGENIERO II','INGENIERO II'),
                ('ARTESANO IV','ARTESANO IV'),
                ('CAJERO/A II','CAJERO/A II'),
                ('OPERAD. EQUIPO ELEC. II','OPERAD. EQUIPO ELEC. II'),
                ('OPERADOR P.A.D. I','OPERADOR P.A.D. I'),
                ('SECRETARIA III','SECRETARIA III'),
                ('SECRETARIA V','SECRETARIA V'),
                ('TEC. EN ABOGACIA II','TEC. EN ABOGACIA II'),
                ('TEC. EN ARCHIVO III','TEC. EN ARCHIVO III'),
                ('TEC. EN ENFERMERIA','TEC. EN ENFERMERIA'),
                ('TEC. EN ENFERMERIA I','TEC. EN ENFERMERIA I'),
                ('TEC. EN FARMACIA I','TEC. EN FARMACIA I'),
                ('TEC. EN TRANSPORTE II','TEC. EN TRANSPORTE II'),
                ('TEC. SANITARIO I','TEC. SANITARIO I'),
                ('ESP. EN SALUD OCUP. I','ESP. EN SALUD OCUP. I'),
                ('TECNICO/A ADMINIST. I','TECNICO/A ADMINIST. I'),
                ('TECNICO/A ADMINIST. II','TECNICO/A ADMINIST. II'),
                ('TECNICO/A ADMINIST. III','TECNICO/A ADMINIST. III'),           
            ]
  
    TIPO_EMPLEADO = [
                ('Nombrado', 'Nombrado'),
                ('Contrato Plazo Fijo', 'Contrato Plazo Fijo'),
                ('Contrato Plazo Indet.', 'Contrato Plazo Indet.'),
                ('Contrato-CAS', 'Contrato-CAS'),
                ('Destacado Externo', 'Destacado Externo'),
                ('CONTRAT. P.S./CAS ASISTENCIAL', 'CONTRAT. P.S./CAS ASISTENCIAL'),            
            ]
    
    REGIMEN_LABORAL = [
                ('D.L. 1057-D.Leg 1057', 'D.L. 1057-D.Leg 1057'),
                ('Nombrado', 'Nombrado'),

            ]
  
    ESTADO = [
                ('Activo', 'Activo'),
                ('Inactivo', 'Inactivo'),
            ]
    
    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                ]
    
    tipo_documento = models.CharField(choices=TIPO_DOCUMENTO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    nombre_completo = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    fecha_nacimiento = models.CharField(max_length=200,null=True, blank=True)
    domicilio = models.CharField(max_length=200,null=True, blank=True)
    genero = models.CharField(choices=GENERO,max_length=100,null=True, blank=True)
    estado_civil = models.CharField(choices=ESTADO_CIVIL,max_length=100,null=True, blank=True)
    unidad_ejecutora = models.CharField(max_length=200,null=True, blank=True)
    unidad_organica = models.CharField(max_length=200,null=True, blank=True)
    unidad_funcional = models.CharField(max_length=200,null=True, blank=True)
    cargo = models.CharField(choices=CARGO,max_length=200,null=True, blank=True)
    condicion_laboral = models.CharField(choices=TIPO_EMPLEADO,max_length=200,null=True, blank=True)
    regimen_laboral = models.CharField(choices=REGIMEN_LABORAL,max_length=200,null=True, blank=True)
    fecha_ingreso = models.CharField(max_length=200,null=True, blank=True)
    fecha_ingreso = models.CharField(max_length=200,null=True, blank=True)	
    horario_ingreso	= models.CharField(max_length=200,null=True, blank=True)
    horario_receso	= models.CharField(max_length=200,null=True, blank=True)
    horario_reingreso = models.CharField(max_length=200,null=True, blank=True)	
    horario_salida = models.CharField(max_length=200,null=True, blank=True)    
    estado = models.CharField(choices=ESTADO,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    foto = models.ImageField(upload_to="img",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.documento_identidad
class Horario(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    horario_ingreso = models.CharField(max_length=200,null=True, blank=True)
    horario_receso = models.CharField(max_length=200,null=True, blank=True)
    horario_reingreso = models.CharField(max_length=200,null=True, blank=True)
    horario_salida = models.CharField(max_length=200,null=True, blank=True)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    hora_salida = models.TimeField()
    hora_salida = models.TimeField()

class Tardanza(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    tardanza = models.DurationField()

class ImportaMarcador(models.Model):
    Tipo_documento = models.CharField(max_length=100,null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=200,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    nombre_completo = models.CharField(max_length=205,null=True, blank=True)
    telefono = models.CharField(max_length=100,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    fecha_nacimiento = models.CharField(max_length=100,null=True, blank=True)
    cargo = models.CharField(max_length=200,null=True, blank=True)
    regimen_laboral = models.CharField(max_length=200,null=True, blank=True)
    fecha_ingreso = models.CharField(max_length=100,null=True, blank=True)
    DNI = models.CharField(max_length=100,null=True, blank=True)
    nombre_completo2 = models.CharField(max_length=200,null=True, blank=True)
    fecha = models.CharField(max_length=100,null=True, blank=True)
    horario_ingreso = models.CharField(max_length=100,null=True, blank=True)
    horario_receso = models.CharField(max_length=100,null=True, blank=True)
    horario_reingreso = models.CharField(max_length=100,null=True, blank=True)
    horario_salida = models.CharField(max_length=100,null=True, blank=True)
    Hora_00_06 = models.CharField(max_length=100,null=True, blank=True)
    Hora_06_07 = models.CharField(max_length=100,null=True, blank=True)
    Hora_07_08 = models.CharField(max_length=100,null=True, blank=True)
    Hora_08_09 = models.CharField(max_length=100,null=True, blank=True)
    Hora_09_10 = models.CharField(max_length=100,null=True, blank=True)
    Hora_10_11 = models.CharField(max_length=100,null=True, blank=True)
    Hora_11_12 = models.CharField(max_length=100,null=True, blank=True)
    Hora_12_13 = models.CharField(max_length=100,null=True, blank=True)
    Hora_13_14 = models.CharField(max_length=100,null=True, blank=True)
    Hora_14_15 = models.CharField(max_length=100,null=True, blank=True)
    Hora_15_16 = models.CharField(max_length=100,null=True, blank=True)
    Hora_16_17 = models.CharField(max_length=100,null=True, blank=True)
    Hora_17_18 = models.CharField(max_length=100,null=True, blank=True)
    Hora_18_19 = models.CharField(max_length=100,null=True, blank=True)
    Hora_19_20 = models.CharField(max_length=100,null=True, blank=True)
    Hora_20_21 = models.CharField(max_length=100,null=True, blank=True)
    Hora_21_22 = models.CharField(max_length=100,null=True, blank=True)
    Hora_22_23 = models.CharField(max_length=100,null=True, blank=True)
    estado_ingreso = models.CharField(max_length=100,null=True, blank=True)
    estado_salida = models.CharField(max_length=100,null=True, blank=True)
    estado_asistencia = models.CharField(max_length=100,null=True, blank=True)
    hora_ingreso_marcador = models.CharField(max_length=100,null=True, blank=True)
    hora_salida_marcador = models.CharField(max_length=100,null=True, blank=True)
    anio = models.CharField(max_length=100,null=True, blank=True)
    mes = models.CharField(max_length=100,null=True, blank=True)
    dia = models.CharField(max_length=100,null=True, blank=True)
    Duracion = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.DNI
    
class MarcadorEmpleado(models.Model):
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    nombre_completo = models.CharField(max_length=250,null=True, blank=True)
    fecha = models.CharField(max_length=250,null=True, blank=True)
    horario_ingreso = models.CharField(max_length=100,null=True, blank=True)
    horario_receso = models.CharField(max_length=100,null=True, blank=True)
    horario_reingreso = models.CharField(max_length=100,null=True, blank=True)
    horario_salida = models.CharField(max_length=100,null=True, blank=True)
    estado_ingreso = models.CharField(max_length=100,null=True, blank=True)
    estado_salida = models.CharField(max_length=100,null=True, blank=True)
    estado_asistencia = models.CharField(max_length=100,null=True, blank=True)
    hora_ingreso_marcador = models.CharField(max_length=100,null=True, blank=True)
    hora_salida_marcador = models.CharField(max_length=100,null=True, blank=True)
    hora_tolerancia = models.CharField(max_length=100,null=True, blank=True)    
    hora_tolerancia_tarde = models.CharField(max_length=100,null=True, blank=True)    
    anio = models.CharField(max_length=100,null=True, blank=True)
    mes = models.CharField(max_length=100,null=True, blank=True)
    dia = models.CharField(max_length=100,null=True, blank=True)
    fecha_marcacion = models.CharField(max_length=100,null=True, blank=True)
    duracion_horas = models.CharField(max_length=100,null=True, blank=True)
    duracion_minutos = models.CharField(max_length=100,null=True, blank=True)
    tardanza = models.CharField(max_length=100,null=True, blank=True)
    tardanza_tarde = models.CharField(max_length=100,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
        
    def __str__(self):
        return self.documento_identidad


class PapeletaHora(models.Model):
    MOTIVO = [
            ('PERSONAL', 'PERSONAL'),
            ('SALUD', 'SALUD'),
            ('PARTICULAR', 'PARTICULAR'),
            ('COMISION', 'COMISION'),
        ]
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    cargo = models.CharField(max_length=100,null=True, blank=True)
    unidad_organica = models.CharField(max_length=100,null=True, blank=True)
    fecha_papeleta_hora = models.CharField(max_length=100,null=True, blank=True)
    anio = models.CharField(max_length=100,null=True, blank=True)
    mes = models.CharField(max_length=100,null=True, blank=True)
    dia = models.CharField(max_length=100,null=True, blank=True)
    hora_salida = models.CharField(max_length=100,null=True, blank=True)
    hora_retorno = models.CharField(max_length=100,null=True, blank=True)
    hora_salida_marcador = models.CharField(max_length=100,null=True, blank=True)
    hora_retorno_marcador = models.CharField(max_length=100,null=True, blank=True)
    motivo = models.CharField(choices=MOTIVO,max_length=250,null=True, blank=True)
    fundamentacion = models.CharField(max_length=250,null=True, blank=True)
    lugar_destino = models.CharField(max_length=250,null=True, blank=True)
    estado_papeleta_dia = models.CharField(max_length=100,null=True, blank=True)
    estado_papeleta_jefe = models.CharField(max_length=100,null=True, blank=True)
    estado_papeleta_rrhh = models.CharField(max_length=100,null=True, blank=True)
    estado_vigilante = models.CharField(max_length=100,null=True, blank=True)
    estado_final = models.CharField(max_length=100,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
        
    def __str__(self):
        return self.documento_identidad

class PapeletaDia(models.Model):
    MOTIVO = [
                ('COMPENSACION DE HORAS EXTRAORDINARIAS', 'COMPENSACION DE HORAS EXTRAORDINARIAS'),
                ('DESCANSO POR ONOMASTICO', 'DESCANSO POR ONOMASTICO'),
                ('DEDUCIBLE DE VACACIONES DEL AÑO', 'DEDUCIBLE DE VACACIONES DEL AÑO'),
                ('LICENCIA POR CAPACITACION OFICIAL', 'LICENCIA POR CAPACITACION OFICIAL'),
                ('PERMISO POR DOCENCIA UNIVERSITARIA', 'PERMISO POR DOCENCIA UNIVERSITARIA'),
                ('LICENCIA POR ENFERMEDAD', 'LICENCIA POR ENFERMEDAD'),
                ('LICENCIA POR SEPELIO Y LUTO (FALLECIMIENTO)', 'LICENCIA POR SEPELIO Y LUTO (FALLECIMIENTO)'),
                ('PERMISO SIN GOSE DE HABER', 'PERMISO SIN GOSE DE HABER'),
                ('POR COMISION DE SERVICIO', 'POR COMISION DE SERVICIO'),
                ('POR CITUACION JUDICIAL', 'POR CITUACION JUDICIAL'),
                ('POR LACTANCIA', 'POR LACTANCIA'),
                ('OTROS (ESPECIFICAR)', 'OTROS (ESPECIFICAR)'),
            ]
    documento_identidad = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True, blank=True)
    cargo = models.CharField(max_length=250,null=True, blank=True)
    unidad_organica = models.CharField(max_length=200,null=True, blank=True)
    fecha_papeleta_dia = models.CharField(max_length=100,null=True, blank=True)
    motivo = models.CharField(choices=MOTIVO,max_length=250,null=True, blank=True)
    fecha_inicio = models.CharField(max_length=100,null=True, blank=True)
    fecha_fin = models.CharField(max_length=100,null=True, blank=True)  
    duracion_dias = models.CharField(max_length=100,null=True, blank=True)
    estado_papeleta_dia = models.CharField(max_length=100,null=True, blank=True)
    estado_papeleta_jefe = models.CharField(max_length=100,null=True, blank=True)
    estado_papeleta_rrhh = models.CharField(max_length=100,null=True, blank=True)
    estado_final = models.CharField(max_length=100,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
        
    def __str__(self):
        return self.documento_identidad
     
    












