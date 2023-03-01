from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from filiacion import views
from filiacion.views import PapeletaHoraPDFView

# Subir archivos estaticos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.home, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    # directorio gobierno local
    path('filiacion/', views.filiacion, name='filiacion'),
    path('filiacion/create/', views.create_filiacion, name='create_filiacion'),
    path('filiacion/<int:filiacion_id>/', views.filiacion_detail, name='filiacion_detail'),
    path('filiacion/<int:filiacion_id>/delete', views.delete_filiacion, name='delete_filiacion'),
    # asistencia #########################
    path('asistencia/', views.listar_asistencias, name='listar_asistencias'),
    # papeletas horas #########################
    path('papeletas_horas/', views.listar_papeleta_horas, name='papeletas_horas'),
    path('papeletas_horas/create/', views.create_papeleta_horas, name='create_papeleta_horas'),
    # autorizacion jefe
    path('bandeja_jefe/', views.listar_bandeja_jefe, name='bandeja_jefe'),
    path('actualizar_estado/<id>/', views.actualizar_estado, name='actualizar_estado'),
    # autorizacion rrhh
    path('bandeja_rrhh/', views.listar_bandeja_rrhh, name='bandeja_rrhh'),
    path('actualizar_estado_rrhh/<id>/', views.actualizar_estado_rrhh, name='actualizar_estado_rrhh'),
    # reporte papeletas horas
    path('papeletas_horas_pdf/<int:papeleta_hora_id>/', PapeletaHoraPDFView.as_view(), name='papeletas_horas_pdf'),
    # papeletas dias #########################
    path('papeletas_dias/', views.listar_papeleta_dias, name='papeletas_dias'),
    path('papeletas_dias/create/', views.create_papeleta_dias, name='create_papeleta_dias'),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)