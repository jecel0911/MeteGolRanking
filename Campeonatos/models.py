# -*- coding: utf-8 -*-
from django.db import models

class Campeonato(models.Model):
	nombre 				= models.CharField(max_length=25)
	fecha_inicio 		= models.DateField()
	fecha_fin 			= models.DateField(blank=True, null=True)
	costo_inscripcion 	= models.DecimalField(max_digits=18,decimal_places=2)
	descripcion 		= models.CharField(max_length=500)
	reglas 				= models.TextField ()
	
	class Meta:
		verbose_name = 'Campeonato'
		verbose_name_plural = 'Campeonatos'

	def __unicode__(self):
		return self.nombre;

	def __str__(self):
		return '%s' % (self.nombre) 	




