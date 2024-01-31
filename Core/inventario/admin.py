"""importando registros"""
from django.contrib import admin

from .models import Computador, DiscoDuro, Mantenimiento, MemoriaRam, Procesador, Tecnico

# Register your models here.

admin.site.register(MemoriaRam)
admin.site.register(DiscoDuro)
admin.site.register(Procesador)
admin.site.register(Tecnico)
admin.site.register(Computador)
admin.site.register(Mantenimiento)