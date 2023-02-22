"""
Serializers from Cliente's app
"""
from clientes.models import Cliente, Endereco
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'nascimento', 'senha']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'cep', 'morador_cliente']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['email', 'senha']
