# -*- coding: utf-8 -*-
from django.db import models

class Player(models.Model):
	id_number = models.CharField(max_length=10)
	player_name = models.CharField(max_length=10)
	last_name_1 = models.CharField(max_length=25)
	last_name_2 = models.CharField(max_length=25)
	nick_name = models.CharField(max_length=25, null=True, blank=True)
	email = models.EmailField()
	points = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Player'
		verbose_name_plural = 'Players'

	def __unicode__(self):
		return self.player_name