from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


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
    titulo = forms.CharField(
        label="Titulo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'})
    )
    
    marca = forms.CharField(
        label="Marca",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la marca'})
    )
    
    modelo = forms.CharField(
        label="Modelo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el modelo'})
    )
    
    yearFabricacion = forms.IntegerField(
        label="Año de fabricación",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el año de fabricación'})
    )
    
    precio = forms.IntegerField(
        label="Precio (en US$)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'})
    )
    
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
        label="Descripción"
    )
    
    telefono = forms.CharField(
        label="Telefono de Contacto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono de contacto'})
    )
    
    email = forms.EmailField(
        label="Email de Contacto",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el email de contacto'})
    )
    
    imagen = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

class UserEditForm(UserChangeForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo electrónico")
    
    password = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# class UserEditPassForm(UserChangeForm):
  
#   password = forms.CharField(
#     help_text="",
#     widget=forms.HiddenInput(), required=False
#   )

#   password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#   password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

#   class Meta:
#     model=User
#     fields=["password1", "password2"]