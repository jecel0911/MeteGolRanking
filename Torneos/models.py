# -*- coding: utf-8 -*-
from django.db import models
from Campeonatos.models import Campeonato

class Torneo(models.Model):

	campeonato 	= models.ForeignKey(Campeonato)
	nombre 		= models.CharField(max_length=25)
	division 	= models.PositiveSmallIntegerField()
	
	class Meta:
		verbose_name = 'Torneo'
		verbose_name_plural = 'Torneos'

	def __unicode__(self):
		return self.nombre;

	def __unicode__(self):
		return 'Campeonato:'+self.campeonato.nombre+',Torneo:'+self.nombre+',division:'+self.division

	def __str__(self):
		return '%s %s %s %s %s %s' % ('Campeonato',self.campeonato.nombre,'Torneo:',self.nombre,'Division:',self.division) 
	

