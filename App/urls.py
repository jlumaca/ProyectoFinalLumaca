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
    path('logout/', LogoutView.as_view(template_name="sesiones/logout.html"),name="Logout"),
    path('registro-user/', views.register,name="Registro"),
    path('editar-user/', views.editUser,name="Editar"),
    path('perfil/', views.perfil,name="Perfil"),
    path('mis-publicaciones/', views.mis_publicaciones,name="MisPublicaciones"),
    path('mi-avatar/', views.mi_avatar,name="MiAvatar"),

    #path('editar-userpass/', views.editUserPass,name="EditarPass"),

    path('about/', views.about,name="About"),

    path('consultar/<str:vehiculo>/<int:id_vehiculo>', views.consultar,name="Consultar"),
    path('responder/<int:id_consulta>/<int:id_vehiculo>', views.responder,name="Responder"),

    path('vehiculos-lista/<str:vehiculo>', views.vehiculos,name="Vehiculos"),
    path('vehiculo-create/<str:vehiculo>', views.vehiculoCreate,name="VehiculoCreate"),
    path('vehiculo-delete/<str:vehiculo>/<int:id_vehiculo>', views.vehiculoDelete,name="VehiculoDelete"),
    path('vehiculo-update/<str:vehiculo>/<int:id_vehiculo>', views.vehiculoUpdate,name="VehiculoUpdate"),
    path('vehiculo-detalles/<str:vehiculo>/<int:id_vehiculo>', views.vehiculoDetail,name="VehiculoDetail"),
    path('vehiculo-search/<str:vehiculo>', views.vehiculoSearch,name="VehiculoSearch"),

    path('publicaciones-admin/', views.publicaciones_admin,name="PublicacionesAdmin"),
    path('consultas-admin/', views.consultas_admin,name="ConsultasAdmin"),
    path('buscar-consultas/', views.buscar_consulta,name="BuscarConsulta"),
    path('censurar-consulta/<int:id_consulta>', views.censurar_consulta,name="CensurarConsulta"),
    path('censurar-respuesta/<int:id_respuesta>', views.censurar_respuesta,name="CensurarRespuesta"),
    path('respuestas-admin/<str:vehiculo>', views.vehiculoSearch,name="VehiculoSearch"),
    path('usuarios-admin/', views.usuarios_admin,name="UsuariosAdmin"),
    path('usuario-delete/<int:id_usuario>', views.usuario_delete,name="UsuarioDelete"),
    path('usuario-update/<int:id_usuario>', views.usuario_update,name="UsuarioUpdate"),
    #path('autos-deleteForm/<id_auto>', views.autoDeleteForm,name="AutoDeleteForm"),

]