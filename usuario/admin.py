from django.contrib import admin

from .models import Usuario
from django.conf import settings

class AdminUsuario(admin.ModelAdmin):
	list_display=('nombreusuario','nombres','apellidos','telefono', 'grupoEmpresarial' )
	#search_fields=('first_name','last_name')


admin.site.register(Usuario, AdminUsuario)
