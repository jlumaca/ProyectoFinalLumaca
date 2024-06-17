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


def autos(req):
    autos = Vehiculo.objects.filter(tipo__icontains="auto")
    return render(req,"autos/autos.html",{"autos":autos})

@login_required
def autoCreate(req):
  if req.method == 'POST':

    miFormulario = PublicarVehiculo(req.POST,req.FILES)

    if miFormulario.is_valid():

      informacion = miFormulario.cleaned_data
      fecha_actual = datetime.now().strftime('%Y-%m-%d')
      #imagen_auto = Vehiculo(imagen=informacion["imagen"])
      nuevo_auto = Vehiculo(titulo = informacion['titulo'],
                            tipo = "auto",
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
      nuevo_auto.save()

      return render(req, "autos/autos_create.html", {"message": "Estudiante ingresado con éxito"})
    
    else:

      return render(req, "autos/autos_create.html", {"error_message": "Datos inválidos"})
  
  else:

    miFormulario = PublicarVehiculo()

    return render(req, "autos/autos_create.html", {"miFormulario": miFormulario})
  
@login_required
def autoDelete(req,id_auto):
    #auto = get_object_or_404(Vehiculo, id=id_auto)
    if req.method == 'POST':

      auto = Vehiculo.objects.get(id=id_auto)
      auto.delete()
      return render(req, "autos/autos_delete.html", {"message":"Auto borrado con éxito","id_auto":0})
      #return HttpResponse(f"<p>{id_auto}</p>")
    else:
       #print(f"Id auto es: {id_auto}")
       return render(req, "autos/autos_delete.html", {"id_auto":id_auto})
       #return HttpResponse(f"<p>{id_auto}</p>")
def autoDeleteForm(req,id_auto):
       return render(req, "autos/autos_delete.html", {"id_auto":id_auto})



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

