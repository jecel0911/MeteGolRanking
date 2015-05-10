# -*- coding: utf-8 -*-
from django.db import models
from Player.models import Player
from Tournement.models import Tournement

# Create your models here.
class Group(models.Model):
	codigo = models.CharField(max_length=50)
	torneo = models.ForeignKey(Tournement)

	class Meta:
		verbose_name = 'Grupo'
		verbose_name_plural = 'Grupos'

	def __unicode__(self):
		return 'Grupo:'+self.codigo

	def __str__(self):
		return '%s %s' % ('Grupo',self.codigo) 
		

class GroupDetail(models.Model):
	grupo = models.ForeignKey(Group)
	jugador = models.ForeignKey(Player)
	puntos = models.DecimalField(max_digits=18,decimal_places=0)
	partidos_jugados = models.DecimalField(max_digits=18,decimal_places=0)
	partidos_ganados = models.DecimalField(max_digits=18,decimal_places=0)
	partidos_perdidos = models.DecimalField(max_digits=18,decimal_places=0)
	goles_a_favor = models.DecimalField(max_digits=18,decimal_places=0)
	goles_en_contra = models.DecimalField(max_digits=18,decimal_places=0)
	goles_de_diferencia = models.DecimalField(max_digits=18,decimal_places=0)
	sets_ganados = models.DecimalField(max_digits=18,decimal_places=0)
	sets_perdidos = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Detalle del grupo'
		verbose_name_plural = 'Detalles del grupo'

	def __unicode__(self):
		return 'Grupo:'+self.grupo.codigo+',Jugador:'+self.jugador.nombre

	def __str__(self):
		return '%s %s %s %s' % ('Grupo',self.grupo.codigo,'Jugador:',self.jugador.nombre) 
		