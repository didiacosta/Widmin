from django.contrib import admin
from .models import AequipoControlador, BGrupoEmpresarial, CSede
# Register your models here.

class AdminAequipoControlador(admin.ModelAdmin):
	list_display=('nombre','ip','nombreUsuario','clave','puerto',)
	search_fields=('nombre',)

admin.site.register(AequipoControlador,AdminAequipoControlador)
