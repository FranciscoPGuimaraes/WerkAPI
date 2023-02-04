"""
Django urls for werkAPI project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('prestadores/', include('prestadores.urls')),
    path('demandas/', include('demandas.urls'))
]
