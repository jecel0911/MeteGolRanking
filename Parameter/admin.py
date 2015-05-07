from django.contrib import admin
from .models import *

class ParameterAdmin(admin.ModelAdmin):
	list_display = ('jugadores_por_division','puntos_ganados_cuando_el_ganador_tiene_mas_puntos',
					'puntos_ganados_cuando_el_ganador_tiene_menos_puntos',
					'puntos_perdidos_cuando_el_perdedor_tiene_mas_puntos',
					'puntos_perdidos_cuando_el_perdedor_tiene_menos_puntos',)
	
	def has_add_permission(self, request, obj=None):
		if Parameter.objects.all().count() == 0:
			return True
		else:
			return False

admin.site.register(Parameter,ParameterAdmin)
