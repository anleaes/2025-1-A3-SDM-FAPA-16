from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Reserva
        fields = ['id', 'codigo', 'cliente', 'status', 'status_display', 'data_criacao']