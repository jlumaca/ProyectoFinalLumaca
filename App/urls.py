from django.contrib import admin
from django.urls import path
from App import views
#from .views import ListaAutos
from django.contrib.auth.views import LogoutView
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.inicio,name="Inicio"),#
   # path('inicio', views.autos,name="Header"),
    path('login/', views.vista_login,name="Login"),
    path('logout/', LogoutView.as_view(template_name="padre.html"),name="Logout"),
    path('registro-user/', views.register,name="Registro"),

    path('autos-lista', views.autos,name="Autos"),
    path('autos-create', views.autoCreate,name="AutoCreate"),
    path('autos-delete/<int:id_auto>', views.autoDelete,name="AutoDelete"),
    path('autos-update/<int:id_auto>', views.autoUpdate,name="AutoUpdate"),
    path('autos-detalle/<int:id_auto>', views.autoDetail,name="AutoDetail"),
    #path('autos-deleteForm/<id_auto>', views.autoDeleteForm,name="AutoDeleteForm"),

]