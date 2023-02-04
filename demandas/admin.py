"""
Models that need appear in admin's interface
"""

from django.contrib import admin
from demandas.models import Demanda

# MODELS
admin.site.register(Demanda)