"""
Urls from Cliente's app
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('login', Cliente_Login),
    path('cadastro', Cliente_Create),
    path('<str:pk>', Cliente_RD),
    path('update', Cliente_Update),
    path('', ClientesALL),
]