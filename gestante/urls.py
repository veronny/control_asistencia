from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from filiacion import views
from filiacion.views import PapeletaHoraPDFView, PapeletaDiaPDFView, RptHojadiarioPDFView, RptHojadiaPDFView, PasswordChangeView, RptPersonalHoraPDFView, RptPersonalHoraNombrePDFView, RptPersonalDiaPDFView, RptPersonalDiaNombrePDFView
from filiacion.views import RptOficinaHoraPDFView, RptOficinaDiaPDFView
# Subir archivos estaticos
from django.conf import settings
from django.conf.urls.static import static
# API Rest Framework
from filiacion.api.router import router_empleado 
from filiacion.api.router import router_papeleta_hora 
from filiacion.api.router import router_papeleta_dia
################################################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.home, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('change_password/', views.PasswordChangeView.as_view(template_name='password_change.html'), name='change_password'),
    path('password_success/', views.password_success, name='password_success'),
    
    
    # directorio gobierno local
    path('filiacion/', views.filiacion, name='filiacion'),
    path('filiacion/create/', views.create_filiacion, name='create_filiacion'),
    path('filiacion/<int:filiacion_id>/', views.filiacion_detail, name='filiacion_detail'),
    path('filiacion/<int:filiacion_id>/delete', views.delete_filiacion, name='delete_filiacion'),
    #################################################################
    
    ############################ asistencia #########################
    path('asistencia/', views.listar_asistencias, name='listar_asistencias'),
    #################################################################
    
    ############################ papeletas horas #########################
    path('papeletas_horas/', views.listar_papeleta_horas, name='papeletas_horas'),
    path('papeletas_horas/create/', views.create_papeleta_horas, name='create_papeleta_horas'),
    path('papeletas_horas/<int:papeleta_hora_id>/', views.papeletas_horas_detail, name='papeletas_horas_detail'),
    # autorizacion jefe
    path('bandeja_jefe/', views.listar_bandeja_jefe, name='bandeja_jefe'),
    path('actualizar_estado/<id>/', views.actualizar_estado, name='actualizar_estado'),
    # autorizacion rrhh
    path('bandeja_rrhh/', views.listar_bandeja_rrhh, name='bandeja_rrhh'),
    path('actualizar_estado_rrhh/<id>/', views.actualizar_estado_rrhh, name='actualizar_estado_rrhh'),
    # reporte papeletas horas
    path('papeletas_horas_pdf/<int:papeleta_hora_id>/', PapeletaHoraPDFView.as_view(), name='papeletas_horas_pdf'),
    ######################################################################
    
    ############################ papeletas dias ##########################
    path('papeletas_dias/', views.listar_papeleta_dias, name='papeletas_dias'),
    path('papeletas_dias/create/', views.create_papeleta_dias, name='create_papeleta_dias'),
    path('papeletas_dias/<int:papeleta_dia_id>/', views.papeletas_dias_detail, name='papeletas_dias_detail'),
    # autorizacion jefe dias
    path('bandeja_jefe_dia/', views.listar_bandeja_jefe_dia, name='bandeja_jefe_dia'),
    path('actualizar_estado_dia/<id>/', views.actualizar_estado_dia, name='actualizar_estado_dia'),
    # autorizacion rrhh dias
    path('bandeja_rrhh_dia/', views.listar_bandeja_rrhh_dia, name='bandeja_rrhh_dia'),
    path('actualizar_estado_rrhh_dia/<id>/', views.actualizar_estado_rrhh_dia, name='actualizar_estado_rrhh_dia'),
    # reporte papeletas dias
    path('papeletas_dias_pdf/<int:papeleta_dia_id>/', PapeletaDiaPDFView.as_view(), name='papeletas_dias_pdf'),
    #####################################################################
    
    ########################### visor vigilante ###################
    path('bandeja_vigilante/', views.listar_bandeja_vigilante, name='bandeja_vigilante'),
    path('actualizar_hora_salida/<id>/', views.actualizar_hora_salida, name='actualizar_hora_salida'),
    path('actualizar_hora_retorno/<id>/', views.actualizar_hora_retorno, name='actualizar_hora_retorno'),
    path('actualizar_estado_vigilante/<id>/', views.actualizar_estado_vigilante, name='actualizar_estado_vigilante'),
    #################################################################
    
    ############################ visor de directores #########################
    # autorizacion directores horas
    path('bandeja_directores/', views.listar_bandeja_directores, name='bandeja_directores'),
    path('actualizar_estado/<id>/', views.actualizar_estado_directores, name='actualizar_estado_directores'),
    # autorizacion directores dias
    path('bandeja_directores_dia/', views.listar_bandeja_directores_dia, name='bandeja_directores_dia'),
    path('actualizar_estado_dia/<id>/', views.actualizar_estado_dia_directores, name='actualizar_estado_dia_directores'),
    ########################################################################
    
    ########################## reportes asistencia ###################
    path('rpt_hoja_diario/', views.rpt_hoja_diario, name='rpt_hoja_diario'),
    # reporte hojas hora
    path('hoja_diario_hora_pdf/', RptHojadiarioPDFView.as_view(), name='hoja_diario_hora_pdf'),
    # reporte hojas dia 
    path('hoja_diario_dia_pdf/', RptHojadiaPDFView.as_view(), name='hoja_diario_dia_pdf'),
    #################################################################
    
    ########################## reportes personal papeleta de salida X DNI #######################
    path('rpt_personal_hora/', views.rpt_personal_hora, name='rpt_personal_hora'),  
    # reporte personal en pdf
    path('rpt_personal_hora_pdf/', RptPersonalHoraPDFView.as_view(), name='rpt_personal_hora_pdf'),
    #############################################################################################
    
    ########################## reportes personal papeleta de salida X NOMBRE ####################
    path('rpt_personal_hora_nombre/', views.rpt_personal_hora_nombre, name='rpt_personal_hora_nombre'),  
    # reporte personal en pdf
    path('rpt_personal_hora_nombre_pdf/', RptPersonalHoraNombrePDFView.as_view(), name='rpt_personal_hora_nombre_pdf'),
    #############################################################################################
    
    ########################## reportes personal papeleta de permiso X DNI ######################
    path('rpt_personal_dia/', views.rpt_personal_dia, name='rpt_personal_dia'),  
    # reporte personal en pdf
    path('rpt_personal_dia_pdf/', RptPersonalDiaPDFView.as_view(), name='rpt_personal_dia_pdf'),
    #############################################################################################
    
    ########################## reportes personal papeleta de permiso X Nombre ######################
    path('rpt_personal_dia_nombre/', views.rpt_personal_dia_nombre, name='rpt_personal_dia_nombre'),  
    # reporte personal en pdf
    path('rpt_personal_dia_nombre_pdf/', RptPersonalDiaNombrePDFView.as_view(), name='rpt_personal_dia_nombre_pdf'),
    #############################################################################################
    
    ########################## reportes oficina ###################
    path('rpt_oficina/', views.rpt_oficina, name='rpt_oficina'),
    # reporte hojas hora
    path('rpt_oficina_hora_pdf/', RptOficinaHoraPDFView.as_view(), name='rpt_oficina_hora_pdf'),
    # reporte hojas dia 
    path('rpt_oficina_dia_pdf/', RptOficinaDiaPDFView.as_view(), name='rpt_oficina_dia_pdf'),
    #################################################################
    
    ########################## dashboard papeletas ###################
    path('dashboard_principal/', views.dashboard_principal, name='dashboard_principal'),
    # reporte hojas hora
    #################################################################
    
    path('api/', include(router_empleado.urls)),
    path('api/ph/', include(router_papeleta_hora.urls)),
    path('api/pd/', include(router_papeleta_dia.urls)),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)