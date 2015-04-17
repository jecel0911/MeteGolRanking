from django.contrib import admin
from models import * 

class PlayerAdmin(admin.ModelAdmin):
	readonly_fields = ('ranking',)
	list_display = ('id_number','player_name','last_name','ranking',)
	#readonly_fields = ('id_number','player_name','last_name','ranking',)
	def a():
		return true

admin.site.register(Player,PlayerAdmin)
