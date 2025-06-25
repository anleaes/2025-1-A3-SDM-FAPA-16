from rest_framework import serializers
from .models import Reserva
from apps.clientes.serializers import ClienteSerializer
from apps.veiculos.serializers import VeiculoSerializer

class ReservaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    veiculo = VeiculoSerializer(read_only=True)
    
    class Meta:
        model = Reserva
        fields = '__all__'