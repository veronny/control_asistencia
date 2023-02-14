from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Filiacion, Red, Microred, Establecimiento, Provincia, Distrito, Empleado, ImportaMarcador

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

# Red
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

#-------------- EMPLEADOS --------------------------
class EmpleadoResources(resources.ModelResource):
    class Meta:
        model = Empleado
@admin.register(Empleado)
class EmpleadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = EmpleadoResources
    list_display = (
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
    search_fields = ('nombres',)    

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