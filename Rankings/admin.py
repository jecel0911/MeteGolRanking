from django.contrib import admin
from .models import *

class RankingAdministrador(admin.ModelAdmin):
	list_display = ('campeonato','jugador','puntos',)

admin.site.register(Ranking,RankingAdministrador)

