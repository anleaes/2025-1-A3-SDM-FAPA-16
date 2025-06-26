from django.db import models
from apps.categorias.models import Categoria

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    class Meta:
        app_label = 'veiculos'
    
    def __str__(self):
        return f"{self.placa} (R${self.valor_diaria}/dia)"