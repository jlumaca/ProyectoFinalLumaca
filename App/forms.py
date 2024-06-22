from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label="Confirme contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme contraseña'})
    )
    imagen = forms.ImageField(
        label="Avatar",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "imagen"]
        help_texts = {k: "" for k in fields}


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

    kilometros = forms.IntegerField(
        label="Kilometros",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los kilometros'})
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

class ConsultaForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre completo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo'}),
        required=False
    )
    
    telefono = forms.CharField(
        label="Telefono",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
        required=False
    )
    
    consulta = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su consulta'}),
        label="Consulta",
        required=False
    )

class ResponderForm(forms.Form):
    respuesta = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su consulta'}),
        label="Respuesta",
        required=False
    )

class AvatarForm(forms.Form):
    imagen = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

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