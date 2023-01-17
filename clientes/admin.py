from django.contrib import admin
from clientes.models import Cliente, Endereco

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Endereco)