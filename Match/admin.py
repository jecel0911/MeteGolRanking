from django.contrib import admin
from Match.models import *


class MatchAdmin(admin.ModelAdmin):
	
	list_display = ('group','jugador_uno','jugador_dos','fecha','set_1_jugador_1','set_1_jugador_2','set_2_jugador_1',
		'set_2_jugador_2','set_3_jugador_1','set_3_jugador_2',)
	def a():
		return true

admin.site.register(Match,MatchAdmin)
