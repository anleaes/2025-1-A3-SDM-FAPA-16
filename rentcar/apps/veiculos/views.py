from rest_framework import viewsets
from .models import Veiculo
from .serializers import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        disponivel = self.request.query_params.get('disponivel')
        if disponivel is not None:
            queryset = queryset.filter(disponivel=disponivel.lower() == 'true')
        return queryset