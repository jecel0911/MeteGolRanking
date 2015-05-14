from django.contrib import admin
from .models import *

class InscripcionAdministrador(admin.ModelAdmin):
	list_display = ('campeonato','jugador','pago',)

admin.site.register(Inscripcion,InscripcionAdministrador)

