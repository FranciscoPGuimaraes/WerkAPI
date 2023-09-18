"""
Views from Demanda's app
"""
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from demandas.models import Demanda
from demandas.serializers import DemandaSerializer
from demandas.serializers import DemandaSerializerID

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
        return Response({'erro': demanda.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Demanda_all(request):
    """
    This function read all demandas in the application
    :param request: pattern param
    :return: information of all demandas
    """
    demanda = Demanda.objects.all()
    demandaSerializer = DemandaSerializerID(demanda, many=True)
    return Response(demandaSerializer.data)


@api_view(['GET'])
def Demanda_Cliente(request, cpf):
    """
    This function read demandas of one cliente
    :param request: pattern param
    :param cpf: foreing key from cliente
    :return: information of all demandas
    """
    try:
        demanda = Demanda.objects.filter(clienteCPF=cpf)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        demandaSerializer = DemandaSerializerID(demanda, many=True)
        return Response(demandaSerializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Demanda_Prestador(request, cpf):
    """
    This function read demandas of one prestador
    :param request: pattern param
    :param cpf: foreing key from prestador
    :return: information of all demandas
    """
    try:
        demanda = Demanda.objects.filter(prestadorCPF=cpf)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        demandaSerializer = DemandaSerializerID(demanda, many=True)
        demandasOrdenadas = sorted(demandaSerializer.data, key=lambda x: int(x['status']))
        return Response(demandasOrdenadas, status=status.HTTP_200_OK)


@api_view(['GET'])
def Demanda_Read(request, id):
    """
    This function read demanda's objects by id
    :param request: pattern param
    :param pk: primary key from demanda
    :return: response status and extra information depending on the request type
    """
    try:
        demanda = Demanda.objects.get(id=id)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        demandaSerializer = DemandaSerializerID(demanda)
        return Response(demandaSerializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Demanda_ReadByType(request, tipo):
    """
    This function read demanda's objects by type
    :param request: pattern param
    :param pk: primary key from demanda
    :return: response status and extra information depending on the request type
    """
    demanda = Demanda.objects.filter(tipo=tipo)
    demandaSerializer = DemandaSerializerID(demanda, many=True)

    if demanda:
        return Response(demandaSerializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def Demanda_UpdateValuePrestador(request):
    """
    This function update preco_max demanda's objects
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status400 and errors if failed
    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        Demanda.objects.filter(id=id).update(preco_max=body['value'], update=1)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def Demanda_UpdateValueCliente(request):
    """
    This function update preco_min demanda's objects
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status400 and errors if failed
    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        Demanda.objects.filter(id=id).update(preco_min=body['value'], update=0)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def Demanda_SetValue(request):
    """
    This function set preco of demanda's objects
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status400 and errors if failed
    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        demanda = Demanda.objects.get(id=id)
        demandaSerializer = DemandaSerializer(demanda)
        if int(demandaSerializer.data["update"]) == 1:
            preco = demandaSerializer.data["preco_max"]
            Demanda.objects.filter(id=id).update(preco=preco, preco_min=preco, status=2)
        elif int(demandaSerializer.data["update"]) == 0:
            preco = demandaSerializer.data["preco_min"]
            Demanda.objects.filter(id=id).update(preco=preco, preco_max=preco, status=2)
    except Demanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(demandaSerializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def Demanda_SetPrestador(request):
    """
    This function set a foreing key of prestador
    :param request: pattern param
    :return: response status201 and the information of Cliente if was successful and status400 and errors if failed
    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        cpf = body['cpf']
        Demanda.objects.filter(id=id).update(prestadroCPF=cpf)
        return Response(status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"Error": str(err)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Demanda_UpdateStatus(request):
    """
    This function update status
    :param request: pattern param
    :param id: primary key of Demanda
    :return: response status201 and the information of Cliente if was successful and status400 and errors if failed
    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        value = body['status']
        Demanda.objects.filter(id=id).update(status=value)
        return Response(status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"Error": str(err)}, status=status.HTTP_400_BAD_REQUEST)