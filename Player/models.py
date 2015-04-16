# -*- coding: utf-8 -*-
from django.db import models

class Player(models.Model):
	shortName = models.CharField(max_length=10)
	ranking = models.DecimalField(max_digits=18,decimal_places=0)

	class Meta:
		verbose_name = 'Player'
		verbose_name_plural = 'Players'

	def __unicode__(self):
		return self.shortName;