from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro', Cliente_Create),
    path('<str:pk>/', Cliente_RUD),
]