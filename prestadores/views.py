from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from prestadores.models import Prestador
from prestadores.serializers import PrestadorSerializers


@api_view(['GET', 'PUT', 'DELETE'])
def Prestador_RUD(request, pk):
    try:
        prestador = Prestador.objects.get(pk=pk)
    except Prestador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Cliente read (Ver o perfil)
        serializer = PrestadorSerializers(prestador)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Cliente update (Atualizar o perfil)
        serializer = PrestadorSerializers(prestador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prestador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def Prestador_Create(request):
    if request.method == 'POST':  # Cliente create (Cadastro)
        serializer = PrestadorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def PrestadorALL(request):
    prestador = Prestador.objects.all()
    serializer = PrestadorSerializers(prestador, many=True)
    return Response(serializer.data)