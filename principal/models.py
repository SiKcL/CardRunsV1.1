from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.CharField(max_length=100, default='General')
    horacreado = models.DateTimeField(default=timezone.now)
    horaactualizado = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class UsuarioNuevo(models.Model):
    nombre= models.CharField(max_length=200)
    contraseña=models.CharField(max_length=200)
    correo=models.EmailField()
    horaregistro=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
