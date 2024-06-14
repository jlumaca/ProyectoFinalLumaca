from django.contrib import admin
from django.urls import path
from App import views
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.inicio,name="Inicio"),#
   # path('inicio', views.autos,name="Header"),
    path('autos-lista', views.autos,name="Autos"),
    path('login', views.vista_login,name="Login"),
]