from django.forms import ModelForm
from .models import Filiacion, PapeletaDia, PapeletaHora
from django import forms
from datetime import datetime, timedelta
#---- cambio de contraseña
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class FiliacionForm(forms.ModelForm):
    class Meta:
       model =  Filiacion       
       fields = [
                 'provincia',
                 'distrito',
                 'tipo_municipalidad',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'provincia' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'distrito' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'tipo_municipalidad' : forms.Select(attrs={'class': 'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }
       
class PapeletaHoraForm(forms.ModelForm):
    class Meta:
       model =  PapeletaHora
       exclude = ['fecha_empleado','fecha_jefe','fecha_rrhh','fecha_vigilante']       
       fields = [
                 'documento_identidad',
                 'nombre_completo',
                 'cargo',
                 'unidad_organica',
                 'condicion_laboral',
                 'regimen_laboral',                
                 'fecha_papeleta_hora',
                 'anio',
                 'mes',
                 'dia',
                 'hora_salida',
                 'motivo',
                 'fundamentacion',
                 'lugar_destino',
                 'estado_papeleta_dia',
                 'estado_papeleta_jefe',
                 'estado_papeleta_rrhh',
                 'estado_vigilante',
                 'user',
                 'rol_unidad_organica',
                 'rol_empleado',
                 'rol_jefe',
                 'rol_rrhh',
                 'rol_vigilante',
                 'firma_empleado',
                 'auditoria_empleado',
                 'firma_jefe', 
                 'auditoria_jefe', 
                 'firma_rrhh',
                 'auditoria_rrhh',
                 'firma_vigilante',
                 'auditoria_vigilante',
                ]     
       widgets = {
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'nombre_completo' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'cargo' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'unidad_organica' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'condicion_laboral' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'regimen_laboral' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'fecha_papeleta_hora' : forms.DateInput(attrs={'type': 'date','class':'form-control','required': True}),
                'anio' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'mes' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'dia' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                #'hora_salida' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}),
                'hora_salida' : forms.TimeInput(attrs={'type': 'time','format':'%H:%M','class':'form-control'}),
                'motivo' : forms.Select(attrs={'class':'form-control','required': True}),
                'fundamentacion' : forms.Textarea(attrs={'class':'form-control','required': True}),
                'lugar_destino' : forms.TextInput(attrs={'class':'form-control','required': True}),
                'user' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_dia' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_jefe' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_rrhh' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_vigilante' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_unidad_organica' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_empleado' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_jefe' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_rrhh' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_vigilante' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                #####################
                 'firma_empleado': forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                 'auditoria_empleado': forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                 'firma_jefe': forms.TextInput(attrs={'class':'form-control','style': 'display: none'}), 
                 'auditoria_jefe':forms.TextInput(attrs={'class':'form-control','style': 'display: none'}), 
                 'firma_rrhh': forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                 'auditoria_rrhh': forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                 'firma_vigilante': forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                 'auditoria_vigilante': forms.TextInput(attrs={'class':'form-control','style': 'display: none'})
       }
       labels = {
            'documento_identidad':'Numero de Documento',
            'nombre_completo':'Apellidos y Nombres',
            'unidad_organica':'Unidad Orgánica',
            'user': '',
            'anio': '',
            'mes': '',
            'dia': '',
            'estado_papeleta_dia': '',
            'estado_papeleta_jefe': '',
            'estado_papeleta_rrhh': '',
            'estado_vigilante': '',
            'fecha_papeleta_hora': 'Fecha',
            'hora_salida': 'Hora Programada',
            'rol_unidad_organica': '',
            'rol_empleado': '',
            'rol_jefe': '',
            'rol_rrhh': '',
            'rol_vigilante': '',
            #####################
            'firma_empleado': '',
            'auditoria_empleado': '',
            'firma_jefe': '', 
            'auditoria_jefe':'', 
            'firma_rrhh': '',
            'auditoria_rrhh': '',
            'firma_vigilante': '',
            'auditoria_vigilante': ''
        }
       
class PapeletaDiaForm(forms.ModelForm):
    
    class Meta:
       model =  PapeletaDia       
       fields = [
                 'documento_identidad',
                 'nombre_completo',
                 'cargo',
                 'condicion_laboral',
                 'regimen_laboral',  
                 'unidad_organica',                              
                 'telefono',                              
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
                 'rol_unidad_organica',
                 'rol_empleado',
                 'rol_jefe',
                 'rol_rrhh',
                 'rol_vigilante'
                ]     
       widgets = {
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'nombre_completo' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'cargo' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'condicion_laboral' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'regimen_laboral' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),               
                'unidad_organica' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),                 
                'telefono' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'fecha_papeleta_dia' : forms.DateInput(attrs={'type': 'date','class':'form-control','style': 'display: none'}),
                'anio' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'mes' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'dia' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'motivo' : forms.Select(attrs={'class':'form-control','required': True}),
                'fundamentacion' : forms.TextInput(attrs={'class':'form-control'}),
                'fecha_inicio' : forms.DateInput(attrs={'type': 'date','class':'form-control','required': True,'id': 'fecha_inicio'}),
                'fecha_fin' : forms.DateInput(attrs={'type': 'date','class':'form-control','required': True,'id': 'fecha_fin','onchange':'calcularDias()'}),
                'duracion_dias' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_dia' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_jefe' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_rrhh' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_final' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'user' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_unidad_organica' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_empleado' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_jefe' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_rrhh' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'rol_vigilante' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'})
       }
       labels = {
            'user': '',
            'anio': '',
            'mes': '',
            'dia': '',
            'estado_papeleta_dia': '',
            'estado_papeleta_jefe': '',
            'estado_papeleta_rrhh': '',
            'motivo': 'Motivo de la solicitud de permiso',
            'fundamentacion': 'Especificar',
            'rol_unidad_organica': '',
            'rol_empleado': '',
            'rol_jefe': '',
            'rol_rrhh': '',
            'rol_vigilante': ''
        }
    
    def clean(self):
        cleaned_data = super(PapeletaDiaForm, self).clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        un_dia = timedelta(days=1)
        fecha_fin_mas_un_dia = fecha_fin + un_dia
        if fecha_inicio and fecha_fin:
            dias = (fecha_fin_mas_un_dia - fecha_inicio).days
            cleaned_data['duracion_dias'] = dias
        return cleaned_data
    

class PasswordChangingForm(PasswordChangeForm):
    
    widgets = {
        'old_password' : forms.PasswordInput(attrs={'class':'form-control'}),
        'old_password' : forms.PasswordInput(attrs={'class':'form-control'}),
        'old_password2' : forms.PasswordInput(attrs={'class':'form-control'})
       }
    #old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña antigua'}))
    #old_passwordold_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña nueva:'}))
    #old_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña nueva (confirmación)'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']