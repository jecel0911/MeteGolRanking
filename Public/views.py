from django.shortcuts import get_object_or_404,render
from django.views import generic

from Rankings.models import Ranking

def index(request):
	lista_jugadores = Ranking.objects.order_by('-puntos')
	context = {'lista_jugadores': lista_jugadores}
	template_name = 'Public/Home.html'
	return render(request,template_name,context)


#Administracion de torneos. acceso para el administrador. 
def torneo(request):
	return render(request,'ad/torneo.html',{})

