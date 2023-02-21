from django.forms import ModelForm
from .models import Filiacion, PapeletaDia, PapeletaHora
from django import forms

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
                ]     
       widgets = {
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'nombre_completo' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'cargo' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'unidad_organica' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'condicion_laboral' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'regimen_laboral' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'fecha_papeleta_hora' : forms.DateInput(attrs={'type': 'date','class':'form-control'}),
                'anio' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'mes' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'dia' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'hora_salida' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}),
                'motivo' : forms.Select(attrs={'class':'form-control'}),
                'fundamentacion' : forms.Textarea(attrs={'class':'form-control'}),
                'lugar_destino' : forms.TextInput(attrs={'class':'form-control'}),
                'user' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_dia' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_jefe' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_papeleta_rrhh' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'}),
                'estado_vigilante' : forms.TextInput(attrs={'class':'form-control','style': 'display: none'})
       }
       labels = {
            'user': '',
            'anio': '',
            'mes': '',
            'dia': '',
            'estado_papeleta_dia': '',
            'estado_papeleta_jefe': '',
            'estado_papeleta_rrhh': '',
            'estado_vigilante': '',
        }