from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    valor_base = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        app_label = 'categorias'
    
    def __str__(self):
        return self.nome