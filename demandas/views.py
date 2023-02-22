"""
Views from Demanda's app
"""
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from demandas.models import Demanda
from demandas.serializers import DemandaSerializer


@api_view(['POST'])
def Demanda_Create(request):
    """
    This function create demanda's objects (register)
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status400 and errors if failed
    """
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        demanda = DemandaSerializer(data=body)
        if demanda.is_valid():
            demanda.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'erro':demanda.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Demanda_all(request):
    """
    This function read all demandas in the application
    :param request: pattern param
    :return: information of all demandas
    """
    demanda = Demanda.objects.all()
    demandaSerializer = DemandaSerializer(demanda, many=True)
    return Response(demandaSerializer.data)


@api_view(['GET'])
def Cliente_Read(request, id):
    """
    This function read, update and delete demanda's objects
    :param request: pattern param
    :param pk: primary key from demanda
    :return: response status and extra information depending on the request type
    """
    try:
        demanda = Demanda.objects.get(id=id)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        demandaSerializer = DemandaSerializer(demanda)
        return Response(demandaSerializer.data, status=status.HTTP_200_OK)



