from django.db import models
from rest_framework import routers
from .user import UserViewSet

class ApiRoot():
	def __init__(self):
		self.router = routers.DefaultRouter()
	
	def runRouter(self):
		#User
		self.router.register(r'users', UserViewSet)
		
		#guarda el resultado en la instancia de la clase. 
		return self.router
