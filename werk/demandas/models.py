from django.db import models
from clientes.models import Cliente
from prestadores.models import Prestador


# Model for cliente table
class Demanda(models.Model):
    tipo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    detalhes = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    data = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )
    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    preco_max = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    preco_min = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    clienteCPF = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    prestadroCPF = models.ForeignKey(
        Prestador,
        on_delete=models.CASCADE,
    )

    objetos = models.Manager()
