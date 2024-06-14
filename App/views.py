from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

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
      psw = data["password"]

      user = authenticate(username=usuario, password=psw)

      if user:
        login(req, user)
        return render(req, "sesiones/login.html", {"message": f"Bienvenido {usuario}"})
      
      else:
        return render(req, "sesiones/login.html", {"error_message": "Datos erroneos"})
    
    else:

      return render(req, "sesiones/login.html", {"error_message": "Datos inválidos"})
  
  else:

    miFormulario = AuthenticationForm()

    return render(req, "sesiones/login.html", {"miFormulario": miFormulario})
