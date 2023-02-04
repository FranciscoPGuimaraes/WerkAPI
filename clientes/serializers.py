"""
Serializers from Cliente's app
"""
from clientes.models import Cliente
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'telefone', 'email', 'nascimento', 'senha']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['email', 'senha']
