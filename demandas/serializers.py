"""
Serializers from Demanda's app
"""
from demandas.models import Demanda
from rest_framework import serializers


class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['tipo', 'descricao', 'detalhes', 'data', 'clienteCPF', 'prestadorCPF', 'preco_max', 'preco_min', 'preco', 'update', 'status']


class DemandaSerializerID(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id', 'tipo', 'descricao', 'detalhes', 'data', 'clienteCPF', 'prestadorCPF', 'preco_max', 'preco_min', 'preco', 'update', 'status']