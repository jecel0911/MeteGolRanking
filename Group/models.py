# -*- coding: utf-8 -*-
from django.db import models
from Player.models import Player
from Tournement.models import Tournement

# Create your models here.
class Group(models.Model):
	player = models.ForeignKey(Player)
	tournement = models.ForeignKey(Tournement)
	code = models.CharField(max_length=50)
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
		verbose_name = 'Group'
		verbose_name_plural = 'Groups'

	def __unicode__(self):
		return 'Group:'+self.code

#class GroupDetail(models.Model):
	#