# -*- coding: utf-8 -*-
from django.db import models 

class Parameter(models.Model):
	jugadores_por_division = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_bono_primer_lugar_torneo = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_bono_segundo_lugar_torneo = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_bono_tercer_lugar_torneo = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_bono_cuarto_lugar_torneo = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_ganados_cuando_el_ganador_tiene_mas_puntos = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_ganados_cuando_el_ganador_tiene_menos_puntos = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_perdidos_cuando_el_perdedor_tiene_mas_puntos = models.DecimalField(max_digits=18,decimal_places=0)
	puntos_perdidos_cuando_el_perdedor_tiene_menos_puntos = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Parametros'
		verbose_name_plural = 'Parametros'

	def __unicode__(self):
		return 'Parametros del Sistema'