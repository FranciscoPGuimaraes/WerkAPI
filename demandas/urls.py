"""
Urls from Demanda's app
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', Demanda_all),
    path('create', Demanda_Create),
    path('<str:id>', Cliente_Read),
]