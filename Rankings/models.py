# -*- coding: utf-8 -*-
from django.db import models
from Campeonatos.models import Campeonato
from Jugadores.models import Jugador


# Create your models here.
class Ranking(models.Model):
	# Esta tabla guarda la lista actual de puntos. 
	# para la primera vez, se crea un campeonato base 0, en el cual se suben los primeros puntos
	# al finalizar el campeonato se actualiza los puntos de acuerdo al campeonato
	campeonato	= models.ForeignKey(Campeonato)
	jugador		= models.ForeignKey(Jugador)
	puntos 		= models.DecimalField(max_digits=18,decimal_places=0)

	
	
	class Meta:
		verbose_name = 'Ranking'
		verbose_name_plural = 'Ranking'

	def __unicode__(self):
		return 'Campeonato:'+self.campeonato.nombre+',Jugador:'+self.jugador.nombre

	def __str__(self):
		return '%s %s %s %s' % ('Campeonato',self.campeonato.nombre,'Jugador:',self.jugador.nombre) 

		
