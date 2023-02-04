"""
Views from Cliente's app
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from clientes.models import Cliente

from clientes.serializers import ClienteSerializer
from clientes.serializers import LoginSerializer


@api_view(['GET'])
def ClientesALL(request):
    """
    This function read all clientes in the application
    :param request: pattern param
    :return: information of all clientes
    """
    cliente = Cliente.objects.all()
    clienteSerializer = ClienteSerializer(cliente, many=True)
    return Response(clienteSerializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def Cliente_RUD(request, pk):
    """
    This function read, update and delete cliente's objects
    :param request: pattern param
    :param pk: primary key from Cliente
    :return: response status and extra information depending on the request type
    """
    try:
        cliente = Cliente.objects.get(cpf=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        clienteSerializer = ClienteSerializer(cliente)
        return Response(clienteSerializer.data)
    elif request.method == 'PUT':
        clienteSerializer = ClienteSerializer(cliente, data=request.data)
        if clienteSerializer.is_valid():
            clienteSerializer.update()
            return Response(clienteSerializer.data, status=status.HTTP_200_OK)
        return Response(clienteSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def Cliente_Create(request):
    """
    This function create cliente's objects (register)
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status201 and errors if failed
    """
    if request.method == 'POST':
        cliente = ClienteSerializer(data=request.data)
        if cliente.is_valid():
            cliente.save()
            return Response(cliente.data, status=status.HTTP_201_CREATED)
        return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Cliente_Login(request):
    """
        Login function
        :param request: pattern param
        :return: response status202 and login status if was successful and response status404 and login status if failed
    """
    login = LoginSerializer(data=request.data)
    if login.is_valid():
        email = login.data.get('email')
        senha = login.data.get('senha')
        cliente = Cliente.objects.filter(email=email, senha=senha)
        if cliente:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
