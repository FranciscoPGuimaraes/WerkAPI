"""
Serializers from Prestador's app
"""
from prestadores.models import Prestador
from rest_framework import serializers


class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['cpf', 'nome', 'telefone', 'email', 'nascimento', 'senha', 'especialidade']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['nome', 'telefone', 'email', 'nascimento']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['email', 'senha']
