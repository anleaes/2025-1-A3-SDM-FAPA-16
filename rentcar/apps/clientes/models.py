from django.db import models

class Cliente(models.Model):
    nome = models.CharField("Nome Completo", max_length=100)
    cpf = models.CharField("CPF", max_length=11, unique=True)
    cnh = models.CharField("CNH", max_length=20, unique=True)  # Novo campo
    telefone = models.CharField("Telefone", max_length=15)
    endereco = models.TextField("Endereço", max_length=200)  # Novo campo
    email = models.EmailField("E-mail", blank=True)  # Opcional (se necessário)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome