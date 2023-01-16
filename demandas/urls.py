from django.urls import path
from .views import *

urlpatterns = [
    path('criar', createDemanda),
    path('', readDemanda),
    path('atualizar', updateDemanda),
    path('demandas', createDemanda),
]