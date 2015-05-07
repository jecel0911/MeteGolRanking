# -*- coding: utf-8 -*-
from django.db import models

class Player(models.Model):
	nombre = models.CharField(max_length=10)
	apellidos = models.CharField(max_length=50)
	apodo = models.CharField(max_length=25, null=True, blank=True)
	email = models.EmailField()
	puntos = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Jugador'
		verbose_name_plural = 'Jugadores'

	def __unicode__(self):
		return self.nombre