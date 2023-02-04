"""
Models that need appear in admin's interface
"""
from django.contrib import admin
from prestadores.models import Prestador

# MODELS
admin.site.register(Prestador)