from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Filiacion, Red, Microred, Establecimiento, Provincia, Distrito, Empleado, ImportaMarcador, MarcadorEmpleado, PapeletaHora, PapeletaDia

#------------Red-------------------------------
admin.site.register(Permission)

# Register your models here.
#------------Red---------------------------------
class RedResources(resources.ModelResource):
    class Meta:
        model = Red

@admin.register(Red)
class RedAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RedResources
    list_display = (
        'id',
        'nombre_red',
        'cod_red',
    )
    search_fields = ('nombre_red',)

#----- MicroRed
admin.site.register(Microred)

#-----------Establecimiento--------------------
class EstablecimientoResources(resources.ModelResource):
    class Meta:
        model = Establecimiento

@admin.register(Establecimiento)
class EstablecimientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = EstablecimientoResources
    list_display = (
        'id',
        'nombre_establecimiento',
        'codigo_unico',
        'red',
        'microred',
    )
    search_fields = ('nombre_establecimiento',)
    
#---------Provincia----------------------------  
class ProvinciaResources(resources.ModelResource):
    class Meta:
        model = Provincia
@admin.register(Provincia)
class ProvinciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ProvinciaResources
    list_display = (
        'id',
        'nombre_provincia',
        'ubigeo',
    )
    search_fields = ('nombre_provincia',)

#------------ Distrito--------------------------
class DistritoResources(resources.ModelResource):
    class Meta:
        model = Distrito

@admin.register(Distrito)
class DistritoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = DistritoResources
    list_display = (
        'id',
        'nombre_distrito',
        'ubigeo',
        'provincia',
    )
    search_fields = ('nombre_distrito',)
    
    
#--------------DIRECTORIO DE MUNICIPIO --------------------------
class FiliacionResources(resources.ModelResource):
    class Meta:
        model = Filiacion

@admin.register(Filiacion)
class FiliacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = FiliacionResources
    list_display = (
        'provincia',
        'distrito',
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'telefono',
        'correo_electronico',
        'condicion',
        'cuenta_usuario'
    )
    search_fields = ('nombres',)
##################################################################
#-------------- EMPLEADOS --------------------------
class EmpleadoResources(resources.ModelResource):
    class Meta:
        model = Empleado
@admin.register(Empleado)
class EmpleadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = EmpleadoResources
    list_display = (
        'id',
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'nombre_completo',
        'telefono',
        'correo_electronico',
        'condicion_laboral',
        'regimen_laboral',
        'estado',
    )
    search_fields = ('documento_identidad','nombres','apellido_paterno',)    

#-------------- MARCADOR --------------------------
class ImportaMarcadorResources(resources.ModelResource):
    class Meta:
        model = ImportaMarcador

@admin.register(ImportaMarcador)
class ImportaMarcadorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    
    resource_class = ImportaMarcadorResources
    list_display = (
        'documento_identidad',
        'nombre_completo',
        'telefono',
        'cargo',
        'regimen_laboral',
        'DNI',
        'horario_ingreso',
        'horario_salida',
        'estado_ingreso',
        'estado_salida',
        'estado_asistencia',
        'hora_ingreso_marcador',
        'hora_salida_marcador',
        'anio',
        'mes',
        'dia',
        'Duracion'
            )
    search_fields = ('DNI',)    
     
#-------------- MARCADOR EMPLEADO ----------------------
class MarcadorEmpleadoResources(resources.ModelResource):
    class Meta:
        model = MarcadorEmpleado

@admin.register(MarcadorEmpleado)
class MarcadorEmpleadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):    
    resource_class = MarcadorEmpleadoResources
    list_display = (
                    'documento_identidad',
                    'nombre_completo',
                    'fecha',
                    'horario_ingreso',
                    'horario_receso',
                    'horario_reingreso',
                    'horario_salida',
                    'estado_ingreso',
                    'estado_salida',
                    'estado_asistencia',
                    'hora_ingreso_marcador',
                    'hora_salida_marcador', 
                    'hora_tolerancia',
                    'anio',
                    'mes',
                    'dia',
                    'duracion_horas',
                    'duracion_minutos',
                    'tardanza'
    )        
    search_fields = ('documento_identidad',)    
       
###################################################### 
#-------------- PAPELETA DE SALIDA HORAS ----------------------
class PapeletaHoraResources(resources.ModelResource):
    class Meta:
        model = PapeletaHora

@admin.register(PapeletaHora)
class PapeletaHoraAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = PapeletaHoraResources
    list_display = (                                                          
                    'id',
                    'documento_identidad',
                    'nombre_completo',
                    'cargo',
                    'unidad_organica',
                    'fecha_papeleta_hora', 
                    'anio',
                    'mes',
                    'dia', 
                    'hora_salida',
                    'hora_retorno',
                    'hora_salida_marcador',
                    'hora_retorno_marcador',
                    'motivo',
                    'fundamentacion',
                    'lugar_destino',
                    'estado_papeleta_dia',
                    'estado_papeleta_jefe',
                    'estado_papeleta_rrhh',
                    'estado_vigilante',
                    'estado_final',
                    'user'
    )
    search_fields = ('id','documento_identidad','nombre_completo','fecha_papeleta_hora',)    
    
########################################################    
#-------------- PAPELETA PERMISO DIAS ----------------------
class PapeletaDiaResources(resources.ModelResource):
    class Meta:
        model = PapeletaDia

@admin.register(PapeletaDia)
class PapeletaDiaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = PapeletaDiaResources
    list_display = (                                                          
                    'id',
                    'documento_identidad',
                    'nombre_completo',
                    'cargo',
                    'condicion_laboral',
                    'regimen_laboral',  
                    'unidad_organica',                              
                    'fecha_papeleta_dia',
                    'anio',
                    'mes',
                    'dia',
                    'motivo',
                    'fundamentacion',
                    'fecha_inicio',
                    'fecha_fin',
                    'duracion_dias',
                    'estado_papeleta_dia',
                    'estado_papeleta_jefe',
                    'estado_papeleta_rrhh',
                    'estado_final',
                    'user',
    )
    search_fields = ('id','documento_identidad','nombre_completo','fecha_papeleta_dia',)    
    
    