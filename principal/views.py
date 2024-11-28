import os
from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post, UsuarioNuevo
from .forms import PostForm, UsuarioLogin
from .forms import UsuarioNuevoForm
from django.core import serializers
import json
# Create your views here.

def inicio(request):
    posts= Post.objects.all()
    return render(request, 'inicio.html',{'posts':posts})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'postear.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm(instance=post)
    return render(request, 'postear.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.imagen:
        imagen_path = os.path.join(settings.MEDIA_ROOT, post.imagen.name)
        if os.path.isfile(imagen_path):
            os.remove(imagen_path)
    post.delete()
    return redirect('inicio')

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioNuevoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a alguna página o muestra un mensaje de éxito
            return redirect('inicio')
    else:
        form = UsuarioNuevoForm()
    return render(request, 'usuarionuevo.html', {'form': form})

def usuario_login(request):
    if request.method == 'POST':
        form = UsuarioLogin(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contraseña = form.cleaned_data['contraseña']
            try:
                usuario = UsuarioNuevo.objects.get(nombre=nombre, contraseña=contraseña)
                request.session['usuario_id'] = usuario.id  # Guardar usuario en la sesión
                return redirect('inicio')
            except UsuarioNuevo.DoesNotExist:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = UsuarioLogin()
    return render(request, 'iniciologin.html', {'form': form})

def usuario_logout(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']  # Eliminar usuario de la sesión
    return redirect('inicio')

def inicio(request):
    usuario = None
    if 'usuario_id' in request.session:
        try:
            usuario = UsuarioNuevo.objects.get(id=request.session['usuario_id'])
        except UsuarioNuevo.DoesNotExist:
            del request.session['usuario_id']  # Eliminar la sesión si el usuario no existe

    posts = Post.objects.all()
    return render(request, 'inicio.html', {'posts': posts, 'usuario': usuario})

