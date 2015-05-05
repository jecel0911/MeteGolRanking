from django.contrib import admin
from .models import * 

class PlayerAdmin(admin.ModelAdmin):
	readonly_fields = ('points',)
	list_display = ('id_number','player_name','last_name_1','last_name_2','email','points',)
	#readonly_fields = ('id_number','player_name','last_name','ranking',)
	def a():
		return true

admin.site.register(Player,PlayerAdmin)
