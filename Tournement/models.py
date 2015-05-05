# -*- coding: utf-8 -*-
from django.db import models

class Tournement(models.Model):
	name = models.CharField(max_length=25)
	begin_date = models.DateTimeField()
	finish_date = models.DateTimeField(blank=True, null=True)
	inscription_cost = models.DecimalField(max_digits=18,decimal_places=2)
	description = models.CharField(max_length=500)
	rules = models.TextField ()
	
	class Meta:
		verbose_name = 'Tournement'
		verbose_name_plural = 'Tournements'

	def __unicode__(self):
		return self.name;




