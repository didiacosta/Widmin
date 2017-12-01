from django.contrib import admin
from .models import AequipoControlador, BGrupoEmpresarial, CSede
# Register your models here.

class AdminAequipoControlador(admin.ModelAdmin):
	list_display=('nombre','ip','nombreUsuario','clave','puerto','created_by','modified_by')
	search_fields=('nombre',)

class AdminBGrupoEmpresarial(admin.ModelAdmin):
	list_display=('nombre','tipo','logoGrupo','equipoControlador','created_by','modified_by')
	search_fields=('nombre','equipoControlador',)
	list_filter=('tipo',)

class AdminCSede(admin.ModelAdmin):
	list_display=('grupoEmpresarial','nombre','logoPropio','logoSede','created_by','modified_by')
	search_fields=('nombre',)
	list_filter=('grupoEmpresarial','logoPropio',)

class AdminDHabitacion(admin.ModelAdmin):
	list_display=('sede__nombre','numero','tipo','created_by','modified_by')


admin.site.register(AequipoControlador,AdminAequipoControlador)
admin.site.register(BGrupoEmpresarial,AdminBGrupoEmpresarial)
admin.site.register(CSede,AdminCSede)
