from django.contrib import admin
from .models import Post
from .models import UsuarioNuevo
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria','horacreado','horaactualizado')
    list_filter = ('categoria',)
    search_fields=('titulo','categoria',)
    ordering = ('-horacreado',)
    
admin.site.register(Post,PostAdmin)


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre','contraseña','correo','horaregistro')
    list_filter = ('horaregistro',)
    search_fields = ('nombre','correo',)
    ordering = ('-horaregistro',)
 
admin.site.register(UsuarioNuevo,UsuariosAdmin)   