from clientes.models import Cliente
from rest_framework import serializers


class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'telefone', 'email', 'nascimento', 'senha']
