# -*- coding: utf-8 -*-
from django.db import models

class Jugador(models.Model):
	nombre = models.CharField(max_length=10)
	apellidos = models.CharField(max_length=50)
	apodo = models.CharField(max_length=25, null=True, blank=True)
	email = models.EmailField()
	
	class Meta:
		verbose_name = 'Jugador'
		verbose_name_plural = 'Jugadores'

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return '%s' % (self.nombre) 
			