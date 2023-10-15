from rest_framework.serializers import ModelSerializer
from filiacion.models import Empleado, PapeletaHora, PapeletaDia

class EmpleadoSerilizer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class PapeletaHoraSerilizer(ModelSerializer):
    class Meta:
        model = PapeletaHora
        fields = '__all__'
        
class PapeletaDiaSerilizer(ModelSerializer):
    class Meta:
        model = PapeletaDia
        fields = '__all__'