from django.db import models
from clientes.models import Cliente

class Reserva(models.Model):
    PENDENTE = 'P'
    CONFIRMADA = 'C'
    CANCELADA = 'X'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDENTE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=10, unique=True)

    def confirmar(self):
        self.status = self.CONFIRMADA
        self.save()

    def __str__(self):
        return f"Reserva #{self.codigo} - {self.get_status_display()}"