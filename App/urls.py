from django.contrib import admin
from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.inicio,name="Inicio"),#
   # path('inicio', views.autos,name="Header"),
    path('login/', views.vista_login,name="Login"),
    path('logout/', LogoutView.as_view(template_name="padre.html"),name="Logout"),
    path('registro-user/', views.register,name="Registro"),
    path('autos-lista', views.autos,name="Autos"),

]