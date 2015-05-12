# -*- coding: utf-8 -*-
from django.db import models

class Torneo(models.Model):
	nombre_del_torneo = models.CharField(max_length=25)
	fecha_de_inicio = models.DateField()
	fecha_de_fin = models.DateField(blank=True, null=True)
	costo_de_la_inscripcion = models.DecimalField(max_digits=18,decimal_places=2)
	descripcion = models.CharField(max_length=500)
	reglas = models.TextField ()
	
	class Meta:
		verbose_name = 'Torneo'
		verbose_name_plural = 'Torneos'

	def __unicode__(self):
		return self.nombre_del_torneo;




