"""
Views from Prestador's app
"""
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from prestadores.models import Prestador
from prestadores.models import Especialidade

from prestadores.serializers import PrestadorSerializer
from prestadores.serializers import LoginSerializer
from clientes.serializers import EnderecoSerializer
from prestadores.serializers import UpdateSerializer
from prestadores.serializers import EspecialidadeSerializer


@api_view(['GET'])
def PrestadorALL(request):
    """
    This function read all prestadores in the application
    :param request: pattern param
    :return: information of all clientes
    """
    prestador = Prestador.objects.all()
    prestadorserializer = PrestadorSerializer(prestador, many=True)
    return Response(prestadorserializer.data)


@api_view(['POST'])
def Prestador_Update(request):
    """
    This function update prestador's objects
    :param request: pattern param
    :return: response status200 if was successful and status404 if not found
    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        serializer = UpdateSerializer(data=body["prestador"])
        cpf = body["cpf"]
        prestador = Prestador.objects.filter(cpf=cpf)
        if serializer.is_valid():
            prestador.update(nome=serializer.data["nome"], telefone=serializer.data["telefone"],
                             email=serializer.data["email"], nascimento=serializer.data["nascimento"])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Prestador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def Prestador_RD(request, pk):
    """
    This function read and delete prestador's objects
    :param request: pattern param
    :param pk: primary key from Cliente
    :return: response status and extra information depending on the request type
    """
    try:
        prestador = Prestador.objects.get(cpf=pk)
    except Prestador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = PrestadorSerializer(prestador)
        return Response(Serializer.data)
    elif request.method == 'DELETE':
        prestador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def Prestador_Create(request):
    """
    This function create prestador's objects (register)
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status201 and errors if failed
    """
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        prestador = PrestadorSerializer(data=body['prestador'])
        endereco = EnderecoSerializer(data=body['endereco'])
        email = body["prestador"]["email"]
        emailExist = Prestador.objects.filter(email=email)
        if not emailExist:
            if prestador.is_valid():
                prestador.validated_data["senha"] = make_password(prestador.validated_data["senha"])
                prestador.save()
                if endereco.is_valid():
                    endereco.save()
                    return Response(status=status.HTTP_201_CREATED)
                return Response({'erro': endereco.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'erro': prestador.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'erro': "Email já existente"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Prestador_Login(request):
    """
        Login function
        :param request: pattern param
        :return: response status202 and login status if was successful and response status404 and login status if failed
    """
    body = json.loads(request.body.decode('utf-8'))
    login = LoginSerializer(data=body)
    if login.is_valid():
        email = login.data.get('email')
        senha = login.data.get('senha')
        prestador = Prestador.objects.get(email=email)
        serializer = PrestadorSerializer(prestador)
        if prestador:
            if check_password(senha, serializer.data["senha"]):
                return Response({'cpf': serializer.data['cpf']}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Especialidade_Create(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        serializer = EspecialidadeSerializer(data=body["especialidade"])

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Especialidade_read(request):
    try:
        especialidades = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(data=especialidades, many=True)
        if serializer:
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
