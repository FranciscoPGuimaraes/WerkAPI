"""
Serializers from Demanda's app
"""
from demandas.models import Demanda
from rest_framework import serializers


class DemandaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id', 'tipo', 'descricao', 'detalhes', 'data', 'preco', 'preco_max', 'preco_min', 'clienteCPF', 'prestadroCPF']