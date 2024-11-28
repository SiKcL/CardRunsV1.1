from django import forms
from principal.models import UsuarioNuevo
from principal.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','contenido','categoria','imagen']
        labels = {
            'titulo':'Titulo',
            'contenido':'Contenido',
            'categoria':'Categoria',
            'imagen' : 'Imagen'
        }
        
class UsuarioNuevoForm(forms.ModelForm):
    class Meta:
        model = UsuarioNuevo
        fields = ['nombre','contraseña','correo']
        labels = {
            'nombre':'Nombre',
            'contenido':'Contenido',
            'correo':'Correo Electronico'
        }

class UsuarioLogin(forms.ModelForm):
    class Meta:
        model = UsuarioNuevo
        fields = ['nombre','contraseña']
        labels = {
            'nombre':'Nombre',
            'contraseña':'Contraseña'
        }