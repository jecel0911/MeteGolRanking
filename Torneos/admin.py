from django.contrib import admin
from .models import *

class TorneoAdministrador(admin.ModelAdmin):
	list_display = ('campeonato','nombre','division',)

admin.site.register(Torneo,TorneoAdministrador)
