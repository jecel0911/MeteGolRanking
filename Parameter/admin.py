from django.contrib import admin
from .models import *

class ParameterAdmin(admin.ModelAdmin):
	list_display = ('players_by_division','points_earned_when_winner_is_higher',
		            'points_earned_when_winner_is_lower','points_earned_when_loser_is_higher',
		            'points_earned_when_loser_is_lower')
	
	def has_add_permission(self, request, obj=None):
		if Parameter.objects.all().count() == 0:
			return True
		else:
			return False

admin.site.register(Parameter,ParameterAdmin)
