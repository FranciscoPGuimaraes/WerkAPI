from prestadores.models import Prestador
from rest_framework import serializers


class PrestadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['cpf', 'nome', 'telefone', 'email', 'nascimento', 'senha', 'especialidade', 'cadastroValidado']