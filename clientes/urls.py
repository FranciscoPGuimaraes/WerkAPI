"""
Urls from Cliente's app
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('login', Cliente_Login),
    path('cadastro', Cliente_Create),
    path('<str:pk>', Cliente_RUD),
    path('', ClientesALL),
]