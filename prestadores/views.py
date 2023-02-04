"""
Views from Prestador's app
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from prestadores.models import Prestador

from prestadores.serializers import PrestadorSerializer
from prestadores.serializers import LoginSerializer


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


@api_view(['GET', 'PUT', 'DELETE'])
def Prestador_RUD(request, pk):
    """
    This function read, update and delete prestador's objects
    :param request: pattern param
    :param pk: primary key from Cliente
    :return: response status and extra information depending on the request type
    """
    try:
        prestador = Prestador.objects.get(cpf=pk)
    except Prestador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        clienteSerializer = PrestadorSerializer(prestador)
        return Response(clienteSerializer.data)
    elif request.method == 'PUT':
        clienteSerializer = PrestadorSerializer(prestador, data=request.data)
        if clienteSerializer.is_valid():
            clienteSerializer.update()
            return Response(clienteSerializer.data, status=status.HTTP_200_OK)
        return Response(clienteSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        prestador = PrestadorSerializer(data=request.data)
        if prestador.is_valid():
            prestador.save()
            return Response(prestador.data, status=status.HTTP_201_CREATED)
        return Response(prestador.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Prestador_Login(request):
    """
        Login function
        :param request: pattern param
        :return: response status202 and login status if was successful and response status404 and login status if failed
    """
    login = LoginSerializer(data=request.data)
    if login.is_valid():
        email = login.data.get('email')
        senha = login.data.get('senha')
        prestador = Prestador.objects.filter(email=email, senha=senha)
        if prestador:
            return Response({"login": True}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"login": False, "erro": "usuario não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
