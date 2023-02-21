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

# Create your views here.
from .forms import FiliacionForm, PapeletaHoraForm
from .models import Filiacion, Empleado, ImportaMarcador,User, MarcadorEmpleado, PapeletaDia, PapeletaHora

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

# ----- PAPELETA HORA --------------------
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