from rest_framework.routers import DefaultRouter
from filiacion.api.views import EmpleadoApiViewSet, PapeletaHoraApiViewSet, PapeletaDiaApiViewSet

router_empleado = DefaultRouter()
router_empleado.register(prefix='empleado', basename='empleado', viewset=EmpleadoApiViewSet)
###################
router_papeleta_hora = DefaultRouter()
router_papeleta_hora.register(prefix='papeleta_hora', basename='papeleta_hora', viewset=PapeletaHoraApiViewSet)
##################
router_papeleta_dia = DefaultRouter()
router_papeleta_dia.register(prefix='papeleta_dia', basename='papeleta_dia', viewset=PapeletaDiaApiViewSet)