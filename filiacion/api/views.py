from rest_framework.viewsets import ModelViewSet
from filiacion.models import Empleado, PapeletaHora, PapeletaDia
from filiacion.api.serializers import EmpleadoSerilizer , PapeletaHoraSerilizer, PapeletaDiaSerilizer

class EmpleadoApiViewSet(ModelViewSet):
    serializer_class = EmpleadoSerilizer 
    queryset = Empleado.objects.all()
    
class PapeletaHoraApiViewSet(ModelViewSet):
    serializer_class = PapeletaHoraSerilizer 
    queryset = PapeletaHora.objects.all()
    
class PapeletaDiaApiViewSet(ModelViewSet):
    serializer_class = PapeletaDiaSerilizer 
    queryset = PapeletaDia.objects.all()