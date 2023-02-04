"""
Serializers from Prestador's app
"""
from prestadores.models import Prestador
from rest_framework import serializers


class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['cpf', 'nome', 'telefone', 'email', 'nascimento', 'senha', 'cadastroValidado', 'especialidade']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['email', 'senha']
