"""
Urls from Demanda's app
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', Demanda_all),
    path('create', Demanda_Create),
    path('atualizarPrestador', Demanda_UpdateValuePrestador),
    path('atualizarCliente', Demanda_UpdateValueCliente),
    path('setValor', Demanda_SetValue),
    path('infos/<str:id>', Demanda_Read),
    path('cliente/<str:cpf>', Demanda_Cliente),
    path('tipo/<str:tipo>', Demanda_ReadByType),
]