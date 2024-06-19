from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from App.forms import UserRegisterForm,PublicarVehiculo
from .models import Vehiculo, Chat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

def inicio(req):
    return render(req,"padre.html",{})

def header(req):
    return render(req,"header.html",{})


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
      return render(req, f"{vehiculo}/{vehiculo}_delete.html", {"message":"Auto borrado con éxito","id_vehiculo":0})
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
          "precio": vehiculoUpd.precio,
          "descripcion": vehiculoUpd.descripcion,
          "telefono": vehiculoUpd.telefonoVendedor,
          "email": vehiculoUpd.emailVendedor,
          "imagen": vehiculoUpd.imagen,
        })

        return render(req, f"{vehiculo}/{vehiculo}_update.html", {"form": Formulario, "id_vehiculo": id_vehiculo})

def vehiculoDetail(req,vehiculo,id_vehiculo):
  vehiculoDet = Vehiculo.objects.get(id=id_vehiculo)
  contexto = {
     "titulo":vehiculoDet.titulo,
     "marca":vehiculoDet.marca,
     "modelo":vehiculoDet.modelo,
     "año":vehiculoDet.anioFabricacion,
     "precio":vehiculoDet.precio,
     "descripcion":vehiculoDet.descripcion,
     "telefono":vehiculoDet.telefonoVendedor,
     "email":vehiculoDet.emailVendedor,
     "imagenVehiculo":vehiculoDet.imagen.url if vehiculoDet.imagen else None
  }
  return render(req, f"{vehiculo}/{vehiculo}_details.html", contexto)


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
        return render(req, "padre.html", {})
      
      else:
        return render(req, "sesiones/login.html", {"error_message": "Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."})
    
    else:
      print(miFormulario.errors)
      return render(req, "sesiones/login.html", {"error_message": "Datos inválidos. Por favor, revisa los campos e inténtalo de nuevo."})
  
  else:

    miFormulario = AuthenticationForm()

    return render(req, "sesiones/login.html", {"miFormulario": miFormulario})

def cerrarsesion(req):
    pass

def register(req):
  if req.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(req.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(req,"sesiones/login.html" ,  {"message":"Usuario Creado :)"})

  else:
            #form = UserCreationForm()       
            form = UserRegisterForm()  

  return render(req,"sesiones/registrarme.html" ,  {"form":form})  



#class ListaAutos(LoginRequiredMixin, ListView):
#    context_object_name = 'autos'
#    queryset = Vehiculo.objects.filter(tipo__startswith='auto')
#    template_name = 'autos/autos.html'
    #login_url = '/login/'

#class GuitarraDetalle(LoginRequiredMixin, DetailView):
#    model = Vehiculo
#    context_object_name = 'guitarra'
#    template_name = 'Base/guitarraDetalle.html'

#class GuitarraUpdate(LoginRequiredMixin, UpdateView):
#    model = Vehiculo
#    form_class = ActualizacionInstrumento
#    success_url = reverse_lazy('guitarras')
#    context_object_name = 'guitarra'
#    template_name = 'Base/guitarraEdicion.html'

#class GuitarraDelete(LoginRequiredMixin, DeleteView):
#    model = Vehiculo
#    success_url = reverse_lazy('guitarras')
#    context_object_name = 'guitarra'
#    template_name = 'Base/guitarraBorrado.html'

