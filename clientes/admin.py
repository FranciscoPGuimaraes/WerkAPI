"""
Models that need appear in admin's interface
"""

from django.contrib import admin
from clientes.models import Cliente, Endereco

#MODELS
admin.site.register(Cliente)
admin.site.register(Endereco)