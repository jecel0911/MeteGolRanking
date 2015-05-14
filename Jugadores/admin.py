from django.contrib import admin
from .models import * 

class JugadorAdministrador(admin.ModelAdmin):
	# readonly_fields = ('points',)
	list_display = ('nombre','apellidos','email',)
	def a():
		return true

admin.site.register(Jugador,JugadorAdministrador)
