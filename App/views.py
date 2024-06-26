from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from App.forms import UserRegisterForm,PublicarVehiculo,UserEditForm,ConsultaForm,ResponderForm,AvatarForm,UsuarioUpdate
from .models import Vehiculo, Chat,Respuesta,AvatarUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
# Create your views here.

def inicio(req):
    return render(req,"inicio.html",{})

def about(req):
    return render(req,"about.html",{})


def vehiculos(req,vehiculo):
    vehiculos = Vehiculo.objects.filter(tipo__icontains=vehiculo)
    return render(req,f"{vehiculo}/{vehiculo}.html",{"vehiculos":vehiculos})

@login_required
def vehiculoCreate(req,vehiculo):
  if req.method == 'POST':

    miFormulario = PublicarVehiculo(req.POST,req.FILES)

    if miFormulario.is_valid():

      informacion = miFormulario.cleaned_data
      fecha_actual = datetime.now().strftime('%Y-%m-%d')
      #imagen_auto = Vehiculo(imagen=informacion["imagen"])
      nuevo_vehiculo = Vehiculo(titulo = informacion['titulo'],
                            tipo = vehiculo,
                            marca = informacion['marca'],
                            modelo = informacion['modelo'],
                            anioFabricacion = informacion['yearFabricacion'],
                            kilometros = informacion['kilometros'],
                            precio = informacion['precio'],
                            descripcion = informacion['descripcion'],
                            fechaPublicacion = fecha_actual,
                            telefonoVendedor = informacion['telefono'],
                            emailVendedor = informacion['email'],
                            imagen = informacion['imagen'],
                            vendedor_id = req.user.id
                            )
      nuevo_vehiculo.save()

      return render(req, f"{vehiculo}/{vehiculo}_create.html", {"message": "Vehiculo publicado con éxito"})
    
    else:

      return render(req, f"{vehiculo}/{vehiculo}_create.html", {"error_message": "Datos inválidos"})
  
  else:

    miFormulario = PublicarVehiculo()
    return render(req, f"{vehiculo}/{vehiculo}_create.html", {"miFormulario": miFormulario})
  
@login_required
def vehiculoDelete(req,vehiculo,id_vehiculo):
    #auto = get_object_or_404(Vehiculo, id=id_auto)
    if req.method == 'POST':

      vehiculoDel = Vehiculo.objects.get(id=id_vehiculo)
      vehiculoDel.delete()
      return render(req, f"{vehiculo}/{vehiculo}_delete.html", {"message":"Vehiculo borrado con éxito","id_vehiculo":0})
      #return HttpResponse(f"<p>{id_auto}</p>")
    else:
       #print(f"Id auto es: {id_auto}")
       return render(req, f"{vehiculo}/{vehiculo}_delete.html", {"id_vehiculo":id_vehiculo})
       #return HttpResponse(f"<p>{id_auto}</p>")

@login_required
def vehiculoUpdate(req,vehiculo,id_vehiculo):
      if req.method == 'POST':

        Formulario = PublicarVehiculo(req.POST,req.FILES)

        if Formulario.is_valid():

          data = Formulario.cleaned_data
          vehiculoUpd = Vehiculo.objects.get(id=id_vehiculo)

          vehiculoUpd.titulo = data["titulo"]
          vehiculoUpd.marca = data["marca"]
          vehiculoUpd.modelo = data["modelo"]
          vehiculoUpd.anioFabricacion = data["yearFabricacion"]
          vehiculoUpd.kilometros = data["kilometros"]
          vehiculoUpd.precio = data["precio"]
          vehiculoUpd.descripcion = data["descripcion"]
          vehiculoUpd.telefonoVendedor = data["telefono"]
          vehiculoUpd.emailVendedor = data["email"]
         
          if 'imagen' in req.FILES:
                vehiculoUpd.imagen = data["imagen"]

          vehiculoUpd.save()

          return render(req, f"{vehiculo}/{vehiculo}_update.html", {"message": "Vehiculo actualizado con éxito","id_vehiculo": id_vehiculo})
        
        else:

          return render(req, f"{vehiculo}/{vehiculo}_update.html", {"message": "Datos inválidos","id_vehiculo": id_vehiculo})
      
      else:

        vehiculoUpd = Vehiculo.objects.get(id=id_vehiculo)

        Formulario = PublicarVehiculo(initial={
          "titulo": vehiculoUpd.titulo,
          "marca": vehiculoUpd.marca,
          "modelo": vehiculoUpd.modelo,
          "yearFabricacion": vehiculoUpd.anioFabricacion,
          "kilometros": vehiculoUpd.kilometros,
          "precio": vehiculoUpd.precio,
          "descripcion": vehiculoUpd.descripcion,
          "telefono": vehiculoUpd.telefonoVendedor,
          "email": vehiculoUpd.emailVendedor,
          "imagen": vehiculoUpd.imagen,
        })

        return render(req, f"{vehiculo}/{vehiculo}_update.html", {"form": Formulario, "id_vehiculo": id_vehiculo})

def vehiculoDetail(req,vehiculo,id_vehiculo):
  vehiculoDet = Vehiculo.objects.get(id=id_vehiculo)

  consultas = Chat.objects.filter(consulta=vehiculoDet)

  contexto = {
     "id_vendedor":vehiculoDet.vendedor.id,
     "id_vehiculo":vehiculoDet.id,
     "titulo":vehiculoDet.titulo,
     "marca":vehiculoDet.marca,
     "modelo":vehiculoDet.modelo,
     "año":vehiculoDet.anioFabricacion,
     "kilometros":vehiculoDet.kilometros,
     "precio":vehiculoDet.precio,
     "descripcion":vehiculoDet.descripcion,
     "telefono":vehiculoDet.telefonoVendedor,
     "email":vehiculoDet.emailVendedor,
     "imagenVehiculo":vehiculoDet.imagen.url if vehiculoDet.imagen else None,
     'consultas': consultas,
  }
  return render(req, f"{vehiculo}/{vehiculo}_details.html", contexto)


def vehiculoSearch(req,vehiculo):
  busqueda = req.GET.get('buscar')

  if req.user.is_superuser:
     renderizar_en = "administrador/publicaciones.html"
     resultados = Vehiculo.objects.filter(titulo__icontains=busqueda)
  else: 
     renderizar_en = f'{vehiculo}/{vehiculo}.html'
     resultados = Vehiculo.objects.filter(titulo__icontains=busqueda,tipo=vehiculo)
  return render(req, renderizar_en, {'vehiculos': resultados})


def vista_login(req):

  if req.method == 'POST':

    miFormulario = AuthenticationForm(req, data=req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario = data["username"]
      password = data["password"]

      user = authenticate(username=usuario, password=password)

      if user:
        login(req, user)
        return render(req, "inicio.html", {})
      
      else:
        return render(req, "sesiones/login.html", {"error_message": "Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."})
    
    else:
      print(miFormulario.errors)
      return render(req, "sesiones/login.html", {"error_message": "Datos inválidos. Por favor, revisa los campos e inténtalo de nuevo."})
  
  else:

    miFormulario = AuthenticationForm()

    return render(req, "sesiones/login.html", {"miFormulario": miFormulario})

def register(req):
  if req.method == 'POST':
            form = UserRegisterForm(req.POST,req.FILES)
            if form.is_valid():  
                  username = form.cleaned_data['username']
                  imagenForm = form.cleaned_data
                  form.save()
                  usuario = User.objects.get(username=username)
                    # avatar = AvatarUsuario.objects.get(usuario=usuario)

                  if 'imagen' in req.FILES:
                    print("LLEGA A LA IMAGEN")
                    imgAvatar = imagenForm["imagen"]
                  else:
                    imgAvatar = False
                    
                  avatar = AvatarUsuario(
                                        imagen = imgAvatar,
                                        usuario = usuario
                                        )
                  avatar.save()

                  FormLogin = AuthenticationForm()
                  return render(req,"sesiones/login.html" ,  {"miFormulario":FormLogin,"user_message":"Usuario creado con exito, ahora puedes iniciar sesión"})    
            else:
              error_message = None
              if 'username' in form.errors and 'already exists' in str(form.errors['username']):
                  error_message = "El usuario ya existe, intente con otro."
              elif 'password2' in form.errors:
                  for error in form.errors['password2']:
                      if 'too short' in error:
                          error_message = "La contraseña es muy corta, debe tener al menos 8 caracteres."
                          break
                      if 'password mismatch' in error:
                          error_message = "Las contraseñas no coinciden."
                          break
              if not error_message:
                  error_message = "Revise los datos que han ingresado, los mismos son incorrectos."
              
              return render(req, "sesiones/registrarme.html", {"form": form, "error_message": error_message})
  else:
            #form = UserCreationForm()  
               
            form = UserRegisterForm()  

            return render(req,"sesiones/registrarme.html" ,  {"form":form})

def perfil(req):  
  return render(req,"sesiones/perfil.html" ,  {})


def mis_publicaciones(req):
  vehiculos = Vehiculo.objects.filter(vendedor=req.user.id)
  return render(req,"sesiones/mis_publicaciones.html",{"vehiculos":vehiculos})




@login_required
def editUser(req):

  usuario = req.user

  if req.method == 'POST':

    miFormulario = UserEditForm(req.POST, instance=req.user)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      if len(data["password1"]) < 8:
          return render(req, "sesiones/editar_usuario.html", {"miFormulario": miFormulario,"error_message": "La contraseña es muy corta, debe tener al menos 8 caracteres."})
      elif data["password1"] != data["password2"]:
         return render(req, "sesiones/editar_usuario.html", {"miFormulario": miFormulario,"error_message": "Las contraseñas no coinciden."})
      else:
        usuario.username = data["username"]
        usuario.email = data["email"]
        #usuario.last_name = data["last_name"]
        usuario.set_password(data["password1"])
        usuario.save()
        return render(req, "sesiones/editar_usuario.html", {"message": "Datos actualizado con éxito"})
    else:

      
      if 'username' in miFormulario.errors and 'already exists' in str(miFormulario.errors['username']):      
        return render(req, "sesiones/editar_usuario.html", {"miFormulario": miFormulario, "error_message": "El usuario ya existe, intente con otro."})
      else:
        return render(req, "sesiones/editar_usuario.html", {"miFormulario": miFormulario, "error_message": "Revise los datos que han ingresado, los mismos son incorrectos."})
  
  else:

    miFormulario = UserEditForm(instance=req.user)

    return render(req, "sesiones/editar_usuario.html", {"miFormulario": miFormulario})

def consultar(req,vehiculo,id_vehiculo):
  if req.method == 'POST':

      Formulario = ConsultaForm(req.POST)

      if Formulario.is_valid():

        informacion = Formulario.cleaned_data
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        #imagen_auto = Vehiculo(imagen=informacion["imagen"])
        vehiculo_cons = Vehiculo.objects.get(id=id_vehiculo)
        print(f"ID de la consulta de vehiculo es: {vehiculo_cons.id}")
        nueva_consulta = Chat(nombreCompleto = informacion["nombre"],
                              telefono = informacion["telefono"],
                              mensaje = informacion["consulta"],
                              consulta = vehiculo_cons,
                              fecha = fecha_actual
                              )
        nueva_consulta.save()

        #return render(req, f"{vehiculo}/{vehiculo}_details.html", {})
        return vehiculoDetail(req,vehiculo,id_vehiculo)
      else:

        return render(req, "consultas/consultar.html", {"error_message": "Datos inválidos"})
  
  else:
    Formulario = ConsultaForm(req.POST)
    return render(req, "consultas/consultar.html", {"miFormulario": Formulario})
  
@login_required
def responder(req,id_consulta,id_vehiculo):
  
  vehiculo_cons = Vehiculo.objects.get(id=id_vehiculo)
  consulta_id = Chat.objects.get(id=id_consulta)
  if req.method == 'POST':

      Formulario = ResponderForm(req.POST)
      

      if Formulario.is_valid():

        informacion = Formulario.cleaned_data
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        #imagen_auto = Vehiculo(imagen=informacion["imagen"])
        
        nueva_respuesta = Respuesta(
                              mensaje = informacion["respuesta"],
                              consulta = consulta_id,
                              fecha = fecha_actual
                              )
        nueva_respuesta.save()

        #return render(req, f"{vehiculo}/{vehiculo}_details.html", {})
        return vehiculoDetail(req,vehiculo_cons.tipo,id_vehiculo)
      else:

        return render(req, "consultas/responder.html", {"error_message": "Datos inválidos"})
  
  else:
    
    titulo = vehiculo_cons.titulo
    consulta_mensaje = consulta_id.mensaje
    Formulario = ResponderForm(req.POST)
    return render(req, "consultas/responder.html", {"miFormulario": Formulario,"titulo":titulo,"consulta":consulta_mensaje})

@login_required
def mi_avatar(req):
  
  usuario = User.objects.get(id=req.user.id)
  avatar_imagen = AvatarUsuario.objects.get(usuario=usuario)
  if req.method == 'POST':

      Formulario = AvatarForm(req.POST,req.FILES)
      

      if Formulario.is_valid():

        accion = req.POST["action"]
        #print(f"Accion es: {accion}")

        informacion = Formulario.cleaned_data

        if accion == "guardar":
          if 'imagen' in req.FILES:
                  avatar_imagen.imagen = informacion["imagen"]
                  avatar_imagen.usuario = usuario
                  avatar_imagen.save()
                  return render(req, "sesiones/avatar.html", {"miFormulario": Formulario,
                                                              "message":"Avatar cargado con éxito",
                                                              "imagenAvatar": avatar_imagen.imagen.url if avatar_imagen.imagen else None})
          else:
            Formulario = AvatarForm()
            return render(req, "sesiones/avatar.html", {"miFormulario": Formulario,
                                                        "error_message":"No has cargado ningún avatar",
                                                        "imagenAvatar": avatar_imagen.imagen.url if avatar_imagen.imagen else None})
        else:
            #SE REALIZA BAJA LOGICA DEL AVATAR
            avatar_imagen.imagen = False
            avatar_imagen.usuario = usuario
            avatar_imagen.save()
            return render(req, "sesiones/avatar.html", {"miFormulario": Formulario,"message":"Avatar eliminado con éxito"})
      else:
        return render(req, "consultas/responder.html", {"error_message": "Datos inválidos"})
  
  else:
    Formulario = AvatarForm()
    return render(req, "sesiones/avatar.html", {"miFormulario": Formulario,"imagenAvatar": avatar_imagen.imagen.url if avatar_imagen.imagen else None})

def publicaciones_admin(req):
   vehiculos = Vehiculo.objects.all()
   return render(req,"administrador/publicaciones.html",{"vehiculos":vehiculos})

def consultas_admin(req):
  consultas = Chat.objects.all()
  return render(req,"administrador/consultas.html",{"consultas":consultas})

def buscar_consulta(req):
    busqueda = req.GET.get('buscar')
    resultados = Chat.objects.filter(mensaje__icontains=busqueda)
    return render(req, "administrador/consultas.html", {'consultas': resultados,"no_encontrado":"No se encontraron datos..."})




def censurar_consulta(req,id_consulta):
   if req.method == 'POST':
    consulta = Chat.objects.get(id=id_consulta)
    consulta.mensaje = "Se ha censurado este comentario"
    consulta.save()
    consultas = Chat.objects.all()
    return render(req,"administrador/consultas.html",{"consultas":consultas})
   else:
     return render(req,"administrador/confirmacion.html",{"id_consulta":id_consulta})

def censurar_respuesta(req,id_respuesta):
   if req.method == 'POST':
    respuesta = Respuesta.objects.get(id=id_respuesta)
    respuesta.mensaje = "Se ha censurado esta respuesta"
    respuesta.save()
    consultas = Chat.objects.all()
    return render(req,"administrador/consultas.html",{"consultas":consultas})
   else:
     return render(req,"administrador/confirmacion.html",{"id_consulta":id_respuesta})

@never_cache
def usuarios_admin(req):
   usuarios = User.objects.filter(is_active=True).order_by('username')
   return render(req,"administrador/usuarios.html",{"usuarios":usuarios})

def usuario_delete(req,id_usuario):
    if req.method == 'POST':
      usuario = User.objects.get(id=id_usuario)
      publicaciones = Vehiculo.objects.filter(vendedor=usuario)
      if publicaciones:
        publicaciones.delete()
        
      usuario.delete()
      usuarios = User.objects.all()


      return render(req,"administrador/confirmacion_usuario.html",{"usuarios":usuarios,"message":"Usuario eliminado con exito"})
    else:
      return render(req,"administrador/confirmacion_usuario.html",{"id_usuario":id_usuario})

def usuario_update(req,id_usuario):
   if req.method == 'POST':
      Formulario = UsuarioUpdate(req.POST)
      if Formulario.is_valid():
        data = Formulario.cleaned_data
        usuario = User.objects.get(id=id_usuario)
        usuario.username = data["username"]
        usuario.email = data["email"]
        usuario.save()
        return render(req, "administrador/usuario_update.html", {"form": Formulario, "id_usuario": id_usuario,"message":"Usuario actualizado con exito"})
      else:
         return render(req, "administrador/usuario_update.html", {"form": Formulario, "id_usuario": id_usuario,"error_message":"Los datos son invalidos"})
   
   else:
      usuario = User.objects.get(id=id_usuario)

      Formulario = UsuarioUpdate(initial={
          "username": usuario.username,
          "email": usuario.email,
        })

      return render(req, "administrador/usuario_update.html", {"form": Formulario, "id_usuario": id_usuario})