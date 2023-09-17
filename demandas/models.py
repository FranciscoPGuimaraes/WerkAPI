"""
Models from Demanda's app
"""
from django.db import models
from clientes.models import Cliente
from prestadores.models import Prestador


# Model for Demanda table
class Demanda(models.Model):
    id = models.IntegerField(
        primary_key=True,
        null=False,
        blank=False,
        auto_created=True
    )
    tipo = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    detalhes = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    data = models.CharField(
        max_length=16,
        null=False,
        blank=False
    )
    update = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        null=True,
        blank=True
    )
    status = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        null=False,
        blank=False
    )
    preco = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        null=True,
        blank=True
    )
    preco_max = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        null=True,
        blank=True
    )
    preco_min = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        null=True,
        blank=True
    )
    clienteCPF = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    prestadorCPF = models.ForeignKey(
        Prestador,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.id
