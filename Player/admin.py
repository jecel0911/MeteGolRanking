from django.contrib import admin
from .models import * 

class PlayerAdmin(admin.ModelAdmin):
	# readonly_fields = ('points',)
	list_display = ('nombre','apellidos','email','puntos',)
	def a():
		return true

admin.site.register(Player,PlayerAdmin)
