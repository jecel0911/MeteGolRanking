# -*- coding: utf-8 -*-
from django.db import models
from Player.models import Player
from Tournement.models import Tournement
from Group.models import Group

class Match(models.Model):
	group = models.ForeignKey(Group)
	player_one = models.ForeignKey(Player,related_name="player_one")
	player_two = models.ForeignKey(Player,related_name="player_two")
	date = models.DateTimeField()
	set_1_player_1 = models.DecimalField(max_digits=18,decimal_places=0)
	set_1_player_2 = models.DecimalField(max_digits=18,decimal_places=0)
	set_2_player_1 = models.DecimalField(max_digits=18,decimal_places=0)
	set_2_player_2 = models.DecimalField(max_digits=18,decimal_places=0)
	set_3_player_1 = models.DecimalField(max_digits=18,decimal_places=0)
	set_3_player_2 = models.DecimalField(max_digits=18,decimal_places=0)


	class Meta:
		verbose_name = 'Match'
		verbose_name_plural = 'Matches'

	def __unicode__(self):
		return 'Match:'+self.player_one.player_name + ' vrs ' + self.player_two.player_name

