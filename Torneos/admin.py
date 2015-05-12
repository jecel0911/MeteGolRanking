from django.contrib import admin
from .models import *

class TorneoAdministrador(admin.ModelAdmin):
	list_display = ('nombre_del_torneo','fecha_de_inicio','descripcion','costo_de_la_inscripcion',)

admin.site.register(Torneo,TorneoAdministrador)
