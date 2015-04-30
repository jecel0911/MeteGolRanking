# -*- coding: utf-8 -*-
from django.db import models
from Player.models import Player
from Tournement.models import Tournement

# Create your models here.
class Group(models.Model):
	code = models.CharField(max_length=50)
	tournement = models.ForeignKey(Tournement)

	class Meta:
		verbose_name = 'Group'
		verbose_name_plural = 'Groups'

	def __unicode__(self):
		return 'Group:'+self.code

class GroupDetail(models.Model):
	group = models.ForeignKey(Group)
	player = models.ForeignKey(Player)
	points = models.DecimalField(max_digits=18,decimal_places=0)
	games_played = models.DecimalField(max_digits=18,decimal_places=0)
	wins = models.DecimalField(max_digits=18,decimal_places=0)
	draws = models.DecimalField(max_digits=18,decimal_places=0)
	looses = models.DecimalField(max_digits=18,decimal_places=0)
	goals_for = models.DecimalField(max_digits=18,decimal_places=0)
	goals_against = models.DecimalField(max_digits=18,decimal_places=0)
	goals_difference = models.DecimalField(max_digits=18,decimal_places=0)
	sets_win = models.DecimalField(max_digits=18,decimal_places=0)
	sets_looses = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Group Detail'
		verbose_name_plural = 'Group Details'

	def __unicode__(self):
		return 'Group:'+self.group.code+',player:'+self.player.player_name