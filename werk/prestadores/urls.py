from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro', createPrestador),
    path('', readPrestador),
    path('atualizar', updatePrestador),
]