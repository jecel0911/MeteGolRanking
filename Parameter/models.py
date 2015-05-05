# -*- coding: utf-8 -*-
from django.db import models 

class Parameter(models.Model):
	players_by_division = models.DecimalField(max_digits=18,decimal_places=0)
	bonus_points_1_place = models.DecimalField(max_digits=18,decimal_places=0)
	bonus_points_2_place = models.DecimalField(max_digits=18,decimal_places=0)
	bonus_points_3_place = models.DecimalField(max_digits=18,decimal_places=0)
	bonus_points_4_place = models.DecimalField(max_digits=18,decimal_places=0)
	earned_points_when_winner_is_higher = models.DecimalField(max_digits=18,decimal_places=0)
	earned_points_when_winner_is_lower = models.DecimalField(max_digits=18,decimal_places=0)
	lost_points_when_loser_is_higher = models.DecimalField(max_digits=18,decimal_places=0)
	lost_points_when_loser_is_lower = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Parameter'
		verbose_name_plural = 'Parameters'

	def __unicode__(self):
		return 'Configuration Parameters'