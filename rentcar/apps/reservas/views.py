from rest_framework import viewsets
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.select_related('cliente', 'veiculo').all()
    serializer_class = ReservaSerializer