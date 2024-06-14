from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from App.forms import UserRegisterForm

# Create your views here.

def inicio(req):
    return render(req,"padre.html",{})

def header(req):
    return render(req,"header.html",{})


def autos(req):
    return render(req,"autos/autos.html",{})


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

