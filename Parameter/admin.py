from django.contrib import admin
from .models import *

class ParameterAdmin(admin.ModelAdmin):
	list_display = ('players_by_division','earned_points_when_winner_is_higher',
		            'earned_points_when_winner_is_lower','lost_points_when_loser_is_higher',
		            'lost_points_when_loser_is_lower')
	
	def has_add_permission(self, request, obj=None):
		if Parameter.objects.all().count() == 0:
			return True
		else:
			return False

admin.site.register(Parameter,ParameterAdmin)
