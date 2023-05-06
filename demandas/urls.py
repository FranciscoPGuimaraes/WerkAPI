"""
Urls from Demanda's app
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', Demanda_all),
    path('create', Demanda_Create),
    path('atualizar', Demanda_UpdateValue),
    path('infos/<str:id>', Demanda_Read),
    path('tipo/<str:tipo>', Demanda_ReadByType),
]