from django.db import models


# Model for cliente table
class Prestador(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        primary_key=True,
        max_length=11,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_digits=45,
        null=False,
        blank=False
    )
    nascimento = models.CharField(
        max_digits=10,
        null=False,
        blank=False
    )
    senha = models.CharField(
        max_digits=45,
        null=False,
        blank=False
    )
    especialidade = models.EmailField(
        max_digits=45,
        null=False,
        blank=False
    )
    cadastroValidade = models.BooleanField()

    objetos = models.Manager()
