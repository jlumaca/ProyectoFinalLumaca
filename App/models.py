from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehiculo(models.Model):
    vehiculoSeleccion = (
    ('autos','Autos'),
    ('motos', 'Motos'),
    ('camionetas','Camionetas'),
    ('camiones','Camiones'),
    ('buses','Buses'),
    ('trailers','Trailers'),
    ('agricolas', 'Agricolas'),
    ('acuaticos', 'Acuaticos'),
    ('otro', 'Otro'),
    )
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=15, choices=vehiculoSeleccion, default='autos')
    marca = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anioFabricacion = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoVendedor = models.CharField(max_length=20)
    emailVendedor = models.EmailField()
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['vendedor', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Chat(models.Model):
    comentario = models.ForeignKey(Vehiculo, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)