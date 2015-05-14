from django.contrib import admin
from .models import *

class CampeonatoAdministrador(admin.ModelAdmin):
	list_display = ('nombre','fecha_inicio','descripcion','costo_inscripcion',)

admin.site.register(Campeonato,CampeonatoAdministrador)
