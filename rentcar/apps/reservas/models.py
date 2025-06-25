from django.db import models
from apps.clientes.models import Cliente
from apps.veiculos.models import Veiculo

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada')
    ])
    
    class Meta:
        app_label = 'reservas'
    
    def __str__(self):
        return f"Reserva #{self.id} - {self.cliente.nome}"