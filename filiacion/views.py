from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import pytz
from datetime import datetime, timedelta
from django.contrib import messages
# Create your views here.
from .forms import FiliacionForm, PapeletaHoraForm, PapeletaDiaForm
from .models import Filiacion, Empleado, ImportaMarcador,User, MarcadorEmpleado, PapeletaDia, PapeletaHora
# reporte
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from django.db.models import Subquery
# Creamos los grupos de usuarios

def home(request):
    return render(request, 'home.html')

# ----- DIRECTORIO MUNICIPIO --------------------
@login_required
def filiacion(request):
    filiaciones = Filiacion.objects.all()
    context = {
                'filiaciones': filiaciones,
                }
    return render(request, 'filiacion.html', context)

@login_required
def create_filiacion(request):
    if request.method == "GET":
        return render(request, 'create_filiacion.html', {
            "form": FiliacionForm
        })
    else:
        try:
            form = FiliacionForm(request.POST, request.FILES)
            new_filiacion = form.save(commit=False)
            new_filiacion.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'create_filiacion.html', {
                "form": FiliacionForm,
                "error": "Error creating task."
            })

@login_required
def filiacion_detail(request, filiacion_id):
    if request.method == 'GET':
        filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
        form = FiliacionForm(instance=filiacion)
        context = {
            'filiacion': filiacion,
            'form': form
        }
        return render(request, 'filiacion_detail.html', context)
    else:
        try:
            filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
            form = FiliacionForm(request.POST,request.FILES, instance=filiacion)
            form.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'filiacion_detail.html', {'filiacion': filiacion, 'form': form, 'error': 'Error actualizar'})

@login_required
def delete_filiacion(request, filiacion_id):
    filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
    if request.method == 'POST':
        filiacion.delete()
        return redirect('filiacion')

# ----- INICIO DE SESION --------------------------------
@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o contraseña es incorrecto"})

        login(request, user)
        return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('filiacion')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password fo not match'
        })
        
################################################################################
################################################################################
# ----- ASISTENCIA --------------------
@login_required
def listar_asistencias(request):
    
    empleados = Empleado.objects.filter(user=request.user)
    
    # Obtener el filtro de mes y año del parámetro GET
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if mes and anio:
        asistencias = MarcadorEmpleado.objects.filter(user=request.user,anio=anio,mes=mes).order_by('-fecha_marcacion','mes')
    else:
        asistencias = MarcadorEmpleado.objects.filter(user=request.user).order_by('-fecha_marcacion','mes')
    
    context = {
                'asistencias': asistencias,
                'empleados': empleados,
            }
        
    return render(request, 'asistencia/asistencia.html', context)

################################################################################
################################################################################
#------- PAPELETA HORA --------------------
@login_required
def listar_papeleta_horas(request): 
    # Obtener el filtro de mes y año del parámetro GET
    valores = ['0','1','2','', None]
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    estado = request.GET.get('estado', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if estado:
        papeletas = PapeletaHora.objects.filter(user=request.user,estado_papeleta_dia=estado).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    elif mes and anio:
        papeletas = PapeletaHora.objects.filter(user=request.user,anio=anio,mes=mes).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    else:
        papeletas = PapeletaHora.objects.filter(user=request.user,estado_papeleta_dia__in=valores).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    context = {
                'papeletas': papeletas,
                'empleados' : empleados
            }
    return render(request, 'papeleta_hora/papeleta_hora.html', context)

@login_required
def create_papeleta_horas(request):
    timezone = pytz.timezone('America/Lima')
    now = datetime.now(tz=timezone)
    
    if request.method == 'POST':
        form = PapeletaHoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Enviado correctamente")
            return redirect('papeletas_horas')
    else:       
        empleados = Empleado.objects.get(user=request.user)
        initial_data = {
            'documento_identidad': empleados.documento_identidad,
            'nombre_completo': empleados.nombre_completo,
            'cargo': empleados.cargo,
            'unidad_organica':empleados.unidad_organica,
            'condicion_laboral': empleados.condicion_laboral,
            'regimen_laboral': empleados.regimen_laboral,
            'fecha_papeleta_hora': now,
            'anio' : now.strftime('%Y'),
            'mes' : now.strftime('%m'),
            'dia' : now.strftime('%d'),
            'hora_salida': now.strftime('%H:%M:%S'),           
            'estado_papeleta_dia': '0',
            'estado_papeleta_jefe': '0',
            'estado_papeleta_rrhh': '0',
            'estado_vigilante': '0',
            'user': empleados.user,
            'rol_unidad_organica': empleados.rol_unidad_organica,
            'rol_empleado': empleados.rol_empleado,
            'rol_jefe': empleados.rol_jefe,
            'rol_rrhh': empleados.rol_rrhh,
            'rol_vigilante': empleados.rol_vigilante  
            }
        form = PapeletaHoraForm(initial=initial_data)
    return render(request, 'papeleta_hora/create_papeleta.html', {'form': form })

@login_required
def papeletas_horas_detail(request, papeleta_hora_id):
    if request.method == 'GET':
        papeleta_hora = get_object_or_404(PapeletaHora, pk=papeleta_hora_id)
        form = PapeletaHoraForm(instance=papeleta_hora)
        context = {
            'papeleta_hora': papeleta_hora,
            'form': form
        }
        return render(request, 'papeleta_hora/papeleta_hora_detail.html', context)
    else:
        try:
            papeleta_hora = get_object_or_404(PapeletaHora, pk=papeleta_hora_id)
            form = PapeletaHoraForm(request.POST, instance=papeleta_hora)
            form.save()
            return redirect('papeletas_horas')
        except ValueError:
            return render(request, 'papeleta_hora/papeleta_hora_detail.html', {'papeleta_hora': papeleta_hora, 'form': form, 'error': 'Error actualizar'})

#------- BANDEJA DE VISTO BUENO DE JEFE --------------------
@login_required
def listar_bandeja_jefe(request):
    # Obtener el filtro de mes y año del parámetro GET
    valores = ['0']
    # Obtener todas las marcaciones o filtrar por mes/año
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')    
     
    if fecha_inicio and fecha_fin:
        empleado_unidad_organica = Empleado.objects.filter(user=request.user).values('unidad_organica')
        papeletas = PapeletaHora.objects.filter(fecha_papeleta_hora__range=[fecha_inicio, fecha_fin]).filter(unidad_organica__in=Subquery(empleado_unidad_organica)).order_by('-id')
        
    elif estado == '':
        empleado_unidad_organica = Empleado.objects.filter(user=request.user).values('unidad_organica')
        papeletas = PapeletaHora.objects.all().filter(unidad_organica__in=Subquery(empleado_unidad_organica)).order_by('-id')

    elif estado:
        empleado_unidad_organica = Empleado.objects.filter(user=request.user).values('unidad_organica')
        papeletas = PapeletaHora.objects.filter(estado_papeleta_dia=estado).filter(unidad_organica__in=Subquery(empleado_unidad_organica)).order_by('-id')
    
    else:
        empleado_unidad_organica = Empleado.objects.filter(user=request.user).values('unidad_organica')
        papeletas = PapeletaHora.objects.filter(estado_papeleta_dia__in=valores).filter(unidad_organica__in=Subquery(empleado_unidad_organica)).order_by('-id')
    
    context = {
                'papeletas': papeletas,
            }   
       
    return render(request, 'bandeja_jefe/bandeja_jefe.html', context)

@login_required
def actualizar_estado(request, id):
    if request.method == 'POST':
        bandeja_jefe = get_object_or_404(PapeletaHora, id=id)
        nuevo_estado = request.POST.get('nuevo_estado')
    
        bandeja_jefe.estado_papeleta_jefe = nuevo_estado
        bandeja_jefe.save()
        return redirect(to="bandeja_jefe")
    
    return render(request, 'bandeja_jefe/bandeja_jefe.html')

#------- BANDEJA DE VISTO BUENO DE RRHH --------------------
@login_required
def listar_bandeja_rrhh(request):
    # Obtener valor inicial para listar
    valores_estado = ['0']
    valores_jefe = ['1']
    # Obtener todas las marcaciones o filtrar por mes/año
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    estado_jefe = request.GET.get('estado_jefe')
    # Obtener todas las marcaciones o filtrar por mes/año
    if fecha_inicio and fecha_fin:
        papeletas = PapeletaHora.objects.filter(fecha_papeleta_hora__range=[fecha_inicio, fecha_fin]).order_by('-id')
    
    elif estado:
        papeletas = PapeletaHora.objects.filter(estado_papeleta_dia=estado).order_by('-id')
    
    elif estado_jefe:
        papeletas = PapeletaHora.objects.filter(estado_papeleta_jefe=estado_jefe).order_by('-id')
        
    else:
        papeletas = PapeletaHora.objects.filter(estado_papeleta_dia=0,estado_papeleta_jefe=1).order_by('-id')
    
    context = {
                'papeletas': papeletas
            }
    
    return render(request, 'bandeja_rrhh/bandeja_rrhh.html', context)

@login_required
def actualizar_estado_rrhh(request, id):
    if request.method == 'POST':
        bandeja_jefe = get_object_or_404(PapeletaHora, id=id)
        nuevo_estado = request.POST.get('nuevo_estado')
    
        bandeja_jefe.estado_papeleta_rrhh = nuevo_estado
        bandeja_jefe.estado_papeleta_dia = nuevo_estado
        bandeja_jefe.save()
        return redirect(to="bandeja_rrhh")
    
    return render(request, 'bandeja_rrhh/bandeja_rrhh.html')

#------- REPORTE PDF PAPELETA HORAS --------------------
class PapeletaHoraPDFView(View):
    def get(self, request, *args, **kwargs):
        try:
            papeleta_hora_id = kwargs['papeleta_hora_id']
            papeleta_hora = PapeletaHora.objects.get(id=papeleta_hora_id)
            template = get_template('asistencia/asistencia_report.html')
            context = {
                'papeleta_hora': papeleta_hora,
                'comp': {
                        'name': 'DIRECCION REGIONAL DE SALUD JUNIN', 
                        'ruc':'9429008070', 
                        'address':'MAS ALLA DE LA VICTORIA'
                    } 
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            
            # Generar el PDF con xhtml2pdf
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            return response 
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('papeletas_horas'))

################################################################################
################################################################################
#------- PAPELETA DIA --------------------
@login_required
def listar_papeleta_dias(request):  
    # Obtener el filtro de mes y año del parámetro GET
    valores = ['0','1','', None]    
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    estado = request.GET.get('estado', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if estado:
        papeletas = PapeletaDia.objects.filter(user=request.user,estado_papeleta_dia=estado).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    elif mes and anio:
        papeletas = PapeletaDia.objects.filter(user=request.user,anio=anio,mes=mes).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    else:
        papeletas = PapeletaDia.objects.filter(user=request.user,estado_papeleta_dia__in=valores).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    context = {
                'papeletas': papeletas,
                'empleados' : empleados
            }
    return render(request, 'papeleta_dia/papeleta_dia.html', context)

@login_required
def create_papeleta_dias(request):
    timezone = pytz.timezone('America/Lima')
    now = datetime.now(tz=timezone)
    
    if request.method == 'POST':
        form = PapeletaDiaForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            un_dia = timedelta(days=1)
            fecha_fin_mas_un_dia = fecha_fin + un_dia
            if fecha_inicio and fecha_fin:
                dias = (fecha_fin_mas_un_dia - fecha_inicio).days
                form.fields['duracion_dias'].initial = dias 
            form.save()
            messages.success(request,"Enviado correctamente")
            return redirect('papeletas_dias')
    else:       
        empleados = Empleado.objects.get(user=request.user)
        initial_data = {
            'documento_identidad': empleados.documento_identidad,
            'nombre_completo': empleados.nombre_completo,
            'cargo': empleados.cargo,
            'condicion_laboral': empleados.condicion_laboral,
            'regimen_laboral': empleados.regimen_laboral,
            'unidad_organica':empleados.unidad_organica,          
            'fecha_papeleta_dia': now,
            'anio' : now.strftime('%Y'),
            'mes' : now.strftime('%m'),
            'dia' : now.strftime('%d'),      
            'estado_papeleta_dia': '0',
            'estado_papeleta_jefe': '0',
            'estado_papeleta_rrhh': '0',
            'estado_final': '0',
            'user': empleados.user           
            }
        form = PapeletaDiaForm(initial=initial_data)
    return render(request, 'papeleta_dia/create_papeleta.html', {'form': form })

@login_required
def papeletas_dias_detail(request, papeleta_dia_id):
    if request.method == 'GET':
        papeleta_dia = get_object_or_404(PapeletaDia, pk=papeleta_dia_id)
        form = PapeletaDiaForm(instance=papeleta_dia)
        context = {
            'papeleta_dia': papeleta_dia,
            'form': form
        }
        return render(request, 'papeleta_dia/papeleta_dia_detail.html', context)
    else:
        try:
            papeleta_dia = get_object_or_404(PapeletaDia, pk=papeleta_dia_id)
            form = PapeletaDiaForm(request.POST, instance=papeleta_dia)
            form.save()
            return redirect('papeletas_dias')
        except ValueError:
            return render(request, 'papeleta_dia/papeleta_dia_detail.html', {'papeleta_dia': papeleta_dia, 'form': form, 'error': 'Error actualizar'})

#------- BANDEJA DE VISTO BUENO DE JEFE DIAS --------------------
@login_required
def listar_bandeja_jefe_dia(request):
    # Obtener el filtro de mes y año del parámetro GET
    valores = ['0']
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    # Obtener todas las marcaciones o filtrar por mes/año
    
    if fecha_inicio and fecha_fin:
        papeletas = PapeletaDia.objects.filter(user=request.user,fecha_papeleta_dia__range=[fecha_inicio, fecha_fin]).order_by('-id')
    elif estado:
        papeletas = PapeletaDia.objects.filter(user=request.user,estado_papeleta_dia=estado).order_by('-id')
    else:
        papeletas = PapeletaDia.objects.filter().order_by('id')
    context = {
                'papeletas': papeletas
            }
    return render(request, 'bandeja_jefe_dia/bandeja_jefe.html', context)

@login_required
def actualizar_estado_dia(request, id):
    if request.method == 'POST':
        bandeja_jefe = get_object_or_404(PapeletaDia, id=id)
        nuevo_estado = request.POST.get('nuevo_estado')
    
        bandeja_jefe.estado_papeleta_jefe = nuevo_estado
        bandeja_jefe.save()
        return redirect(to="bandeja_jefe_dia")
    
    return render(request, 'bandeja_jefe_dia/bandeja_jefe.html')

#------- BANDEJA DE VISTO BUENO DE RRHH DIAS --------------------
@login_required
def listar_bandeja_rrhh_dia(request):
    # Obtener el filtro de mes y año del parámetro GET
    valores_estado = ['0','1']
    valores_jefe = ['0','1']
    # Obtener todas las marcaciones o filtrar por mes/año
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    estado_jefe = request.GET.get('estado_jefe')
    # Obtener todas las marcaciones o filtrar por mes/año
    # Obtener todas las marcaciones o filtrar por mes/año
    if fecha_inicio and fecha_fin:
        papeletas = PapeletaDia.objects.filter(user=request.user,fecha_papeleta_dia__range=[fecha_inicio, fecha_fin]).order_by('-id')
    elif estado:
        papeletas = PapeletaDia.objects.filter(user=request.user,estado_papeleta_dia=estado).order_by('-id')
    elif estado_jefe:
        papeletas = PapeletaDia.objects.filter(user=request.user,estado_papeleta_jefe=estado_jefe).order_by('-id')
    else:
        papeletas = PapeletaDia.objects.filter(estado_papeleta_dia__in=valores_estado,estado_papeleta_jefe__in=valores_jefe).order_by('-id')
    context = {
                'papeletas': papeletas
            }
    return render(request, 'bandeja_rrhh_dia/bandeja_rrhh.html', context)

@login_required
def actualizar_estado_rrhh_dia(request, id):
    if request.method == 'POST':
        bandeja_jefe = get_object_or_404(PapeletaDia, id=id)
        nuevo_estado = request.POST.get('nuevo_estado')
    
        bandeja_jefe.estado_papeleta_rrhh = nuevo_estado
        bandeja_jefe.estado_final = nuevo_estado
        bandeja_jefe.estado_papeleta_dia = nuevo_estado
        bandeja_jefe.save()
        return redirect(to="bandeja_rrhh_dia")
    
    return render(request, 'bandeja_rrhh_dia/bandeja_rrhh.html')

#------- REPORTE PDF PAPELETA HORAS --------------------
class PapeletaDiaPDFView(View):
    def get(self, request, *args, **kwargs):
        try:
            papeleta_dia_id = kwargs['papeleta_dia_id']
            papeleta_dia = PapeletaDia.objects.get(id=papeleta_dia_id)
            template = get_template('papeleta_dia/papeleta_dia_report.html')
            context = {
                'papeleta_dia': papeleta_dia,
                'comp': {
                        'name': 'DIRECCION REGIONAL DE SALUD JUNIN', 
                        'ruc':'9429008070', 
                        'address':'MAS ALLA DE LA VICTORIA'
                    } 
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            
            # Generar el PDF con xhtml2pdf
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            return response 
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('papeletas_dias'))
    
################################################################################
################################################################################
#------- VISOR DE VIGILANCIA --------------------
@login_required
def listar_bandeja_vigilante(request):
    # Obtener el filtro de mes y año del parámetro GET
    valores_estado = ['0','1']
    valores_jefe = ['0','1']
    # Obtener todas las marcaciones o filtrar por mes/año
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    estado_jefe = request.GET.get('estado_jefe')
    # Obtener todas las marcaciones o filtrar por mes/año
    if fecha_inicio and fecha_fin:
        papeletas = PapeletaHora.objects.filter(fecha_papeleta_hora__range=[fecha_inicio, fecha_fin],estado_papeleta_rrhh=1).order_by('-id')
    elif estado:
        papeletas = PapeletaHora.objects.filter(estado_papeleta_dia=estado,estado_papeleta_rrhh=1).order_by('-id')
    elif estado_jefe:
        papeletas = PapeletaHora.objects.filter(estado_papeleta_jefe=estado_jefe,estado_papeleta_rrhh=1).order_by('-id')
    else:
        papeletas = PapeletaHora.objects.filter(estado_papeleta_rrhh=1,estado_vigilante=0).order_by('-id')
    context = {
                'papeletas': papeletas
            }
    return render(request, 'bandeja_vigilante/bandeja_vigilante.html', context)


@login_required
def actualizar_hora_salida(request, id):
    if request.method == 'POST':
        bandeja_vigilante = get_object_or_404(PapeletaHora, id=id)
        hora_salida = request.POST.get('hora_salida')
        bandeja_vigilante.hora_salida_marcador = hora_salida
        bandeja_vigilante.save()
        return redirect(to="bandeja_vigilante")
    
    return render(request, 'bandeja_vigilante/bandeja_vigilante.html')

@login_required
def actualizar_hora_retorno(request, id):
    if request.method == 'POST':
        bandeja_vigilante = get_object_or_404(PapeletaHora, id=id)
        hora_retorno = request.POST.get('hora_retorno')
    
        bandeja_vigilante.hora_retorno_marcador = hora_retorno
        bandeja_vigilante.save()
        return redirect(to="bandeja_vigilante")
    
    return render(request, 'bandeja_vigilante/bandeja_vigilante.html')

@login_required
def actualizar_estado_vigilante(request, id):
    if request.method == 'POST':
        bandeja_jefe = get_object_or_404(PapeletaHora, id=id)
        nuevo_estado = request.POST.get('nuevo_estado')
    
        bandeja_jefe.estado_vigilante = nuevo_estado
        bandeja_jefe.save()
        return redirect(to="bandeja_vigilante")
    
    return render(request, 'bandeja_vigilante/bandeja_vigilante.html')

################################################################################
################################################################################
#------- REPORTE DE ASISTENCIA --------------------

