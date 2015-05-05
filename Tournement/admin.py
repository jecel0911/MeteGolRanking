from django.contrib import admin
from .models import *

class TournementAdmin(admin.ModelAdmin):
	list_display = ('name','description','inscription_cost',)

admin.site.register(Tournement,TournementAdmin)
