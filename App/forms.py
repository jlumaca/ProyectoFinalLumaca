from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo electrónico")
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}

class PublicarVehiculo(forms.Form):
    titulo = forms.CharField(label="Titulo")
    
    marca = forms.CharField(label="Marca")
    modelo = forms.CharField(label="modelo")
    yearFabricacion = forms.IntegerField(label="Año de fabricación")
    precio = forms.IntegerField(label="Precio (en US$)")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")
    telefono = forms.CharField(label="Telefono de Contacto")
    email = forms.EmailField(label="Email de Contacto")
    imagen = forms.ImageField(label="Imagen",required=False)