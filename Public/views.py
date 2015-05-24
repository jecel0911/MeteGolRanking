from django.shortcuts import get_object_or_404,render
from django.views import generic


def index(request):
	template_name = 'Public/Home.html'
	return render(request,template_name)

