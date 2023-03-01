from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import pytz
from datetime import datetime
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
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

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
    # papeletas = PapeletaHora.objects.all()   
    # Obtener el filtro de mes y año del parámetro GET
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if mes and anio:
        papeletas = PapeletaHora.objects.filter(user=request.user,anio=anio,mes=mes).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    else:
        papeletas = PapeletaHora.objects.filter(user=request.user).order_by('-id')
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
            'user': empleados.user           
            }
        form = PapeletaHoraForm(initial=initial_data)
    return render(request, 'papeleta_hora/create_papeleta.html', {'form': form })

#------- BANDEJA DE VISTO BUENO DE JEFE --------------------
@login_required
def listar_bandeja_jefe(request):
    # Obtener el filtro de mes y año del parámetro GET
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if mes and anio:
        papeletas = PapeletaHora.objects.filter(anio=anio,mes=mes).order_by('-id')
    else:
        papeletas = PapeletaHora.objects.filter().order_by('id')
    context = {
                'papeletas': papeletas
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
    # Obtener el filtro de mes y año del parámetro GET
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if mes and anio:
        papeletas = PapeletaHora.objects.filter(anio=anio,mes=mes).order_by('-id')
    else:
        papeletas = PapeletaHora.objects.filter().order_by('id')
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
        bandeja_jefe.estado_vigilante = nuevo_estado
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
    anio = request.GET.get('anio', None)
    mes = request.GET.get('mes', None)
    # Obtener todas las marcaciones o filtrar por mes/año
    if mes and anio:
        papeletas = PapeletaDia.objects.filter(user=request.user,anio=anio,mes=mes).order_by('-id')
        empleados = Empleado.objects.filter(user=request.user)
    else:
        papeletas = PapeletaDia.objects.filter(user=request.user).order_by('-id')
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