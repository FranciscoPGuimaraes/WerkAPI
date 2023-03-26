"""
Serializers from Demanda's app
"""
from demandas.models import Demanda
from rest_framework import serializers


class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['tipo', 'descricao', 'detalhes', 'data', 'clienteCPF', 'preco_max', 'preco_max']
