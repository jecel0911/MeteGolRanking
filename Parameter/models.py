# -*- coding: utf-8 -*-
from django.db import models

class Parameter(models.Model):
	players_by_division = models.DecimalField(max_digits=18,decimal_places=0)
	points_earned_when_winner_is_higher = models.DecimalField(max_digits=18,decimal_places=0)
	points_earned_when_winner_is_lower = models.DecimalField(max_digits=18,decimal_places=0)
	points_earned_when_loser_is_higher = models.DecimalField(max_digits=18,decimal_places=0)
	points_earned_when_loser_is_lower = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Parameter'
		verbose_name_plural = 'Parameters'

	def __unicode__(self):
		return 'Configuration Parameters'