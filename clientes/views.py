from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from clientes.models import Cliente
from clientes.serializers import ClienteSerializers


@api_view(['GET', 'PUT', 'DELETE'])
def Cliente_RUD(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Cliente read (Ver o perfil)
        serializer = ClienteSerializers(cliente)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Cliente update (Atualizar o perfil)
        serializer = ClienteSerializers(Cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def Cliente_Create(request):
    if request.method == 'POST':  # Cliente create (Cadastro)
        serializer = ClienteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def Cliente_Login(request):
    try:
        cliente = Cliente.objects.get(email=request.data.email, senha=request.data.senha)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    finally:
        return Response({logged:True} ,status=status.HTTP_200_OK)


@api_view(['GET'])
def ClientesALL(request):
    cliente = Cliente.objects.all()
    serializer = ClienteSerializers(cliente, many=True)
    return Response(serializer.data)