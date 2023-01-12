from django.db import models
from prestadores.models import Prestador


# Model for cliente table
class Cliente(models.Model):
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


# Model for Endereco table
class Endereco(models.Model):
    id = models.IntegerField(
        primary_key=True,
        auto_created=True,
        null=False,
        blank=False
    )
    estado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cidade = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    rua = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    numero = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    complemento = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    cep = models.CharField(
        max_length=9,
        null=False,
        blank=False
    )
    morador_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    morador_prestador = models.ForeignKey(
        Prestador,
        on_delete=models.CASCADE,
    )

    objetos = models.Manager()