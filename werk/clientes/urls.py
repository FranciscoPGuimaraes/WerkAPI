from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro', createCliente),
    path('', readCliente),
    path('atualizar', updateCliente),
]