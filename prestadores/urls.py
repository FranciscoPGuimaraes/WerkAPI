"""
Urls from Prestador's app
"""
from django.urls import path
from prestadores.views import *

urlpatterns = [
    path('login', Prestador_Login),
    path('cadastro', Prestador_Create),
    path('update', Prestador_Update),
    path('', PrestadorALL),
    path('<str:pk>', Prestador_RD),
    path('especialidades', Especialidade_read),
    path('especialidades/cadastro', Especialidade_read),
]