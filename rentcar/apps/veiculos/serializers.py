from rest_framework import serializers
from apps.veiculos.models import Veiculo
from apps.categorias.serializers import CategoriaSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']

class VeiculoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'valor_diaria', 'disponivel', 'categoria']