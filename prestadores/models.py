from django.db import models


# Model for cliente table
class Prestador(models.Model):
    nome = models.CharField(
        max_length=90,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        primary_key=True,
        max_length=13,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=16,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=70,
        null=False,
        blank=False
    )
    nascimento = models.CharField(
        max_length=16,
        null=False,
        blank=False
    )
    senha = models.CharField(
        max_length=25,
        null=False,
        blank=False
    )
    especialidade = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    cadastroValidade = models.BooleanField()

    def __str__(self):
        return self.nome

    objetos = models.Manager()
