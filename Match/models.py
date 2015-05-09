# -*- coding: utf-8 -*-
from django.db import models
from Player.models import Player
from Tournement.models import Tournement
from Group.models import Group

class Match(models.Model):
	group = models.ForeignKey(Group)
	jugador_uno = models.ForeignKey(Player,related_name="player_one")
	jugador_dos = models.ForeignKey(Player,related_name="player_two")
	fecha = models.DateField()
	set_1_jugador_1 = models.DecimalField(max_digits=18,decimal_places=0)
	set_1_jugador_2 = models.DecimalField(max_digits=18,decimal_places=0)
	set_2_jugador_1 = models.DecimalField(max_digits=18,decimal_places=0)
	set_2_jugador_2 = models.DecimalField(max_digits=18,decimal_places=0)
	set_3_jugador_1 = models.DecimalField(max_digits=18,decimal_places=0)
	set_3_jugador_2 = models.DecimalField(max_digits=18,decimal_places=0)


	class Meta:
		verbose_name = 'Partido'
		verbose_name_plural = 'Partidos'

	def __unicode__(self):
		return 'Partido:'+self.jugador_uno.nombre + ' vrs ' + self.jugador_dos.nombre

