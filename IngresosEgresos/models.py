# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class ConceptosIngEgr(models.Model):
	codigo 		= models.CharField(max_length=5)
	descripcion = models.CharField(max_length=50)
	# I= ingreso, E=egreso  se muestra con un radio button
	tipo 		= models.CharField(max_length=1) 
    
	
	class Meta:
		verbose_name = 'Concepto Ingresos/Egresos'
		verbose_name_plural = 'Conceptos Ingresos/Egresos'

	def __unicode__(self):
		return self.descripcion

	def __str__(self):
		return '%s %s' % ('',self.descripcion) 
		

class IngresosEgresos(models.Model):
	concepto 		= models.ForeignKey(ConceptosIngEgr)
	fecha 			= models.DateField()
	monto 			= models.DecimalField(max_digits=18,decimal_places=0)
	descripcion 	= models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Ingreso y Egreso'
		verbose_name_plural = 'Ingresos y Egresos'

	def __unicode__(self):
		return 'Concepto:'+self.concepto.tipo+',monto:'+self.monto+', '+self.descripcion

	def __str__(self):
		return '%s %s %s %s %s %s' % ('Concepto',self.concepto.tipo,'monto:',self.monto,' ',self.descripcion) 
		