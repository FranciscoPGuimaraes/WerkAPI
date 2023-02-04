"""
Urls from Prestador's app
"""
from django.urls import path
from prestadores.views import *

urlpatterns = [
    path('login', Prestador_Login),
    path('cadastro', Prestador_Create),
    path('<str:pk>', Prestador_RUD),
    path('', PrestadorALL),
]