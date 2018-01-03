from django.contrib import admin
from .models import APersona, BHuesped
# Register your models here.

class AdminAPersona(admin.ModelAdmin):
	list_display=('identificacion','tipoIdentificacion','nombres','apellidos','fechaNacimiento','genero')
	search_fields=('nombres','apellidos','identificacion')
	list_filter=('genero','tipoIdentificacion')

class AdminBHuesped(admin.ModelAdmin):
	list_display=('identificacion','persona','fechaEntrada','fechaSalida','acompananteDe'
		,'habitacion')
	search_fields=('habitacion','persona')
	list_filter=('fechaEntrada','fechaSalida')


admin.site.register(APersona,AdminAPersona)
admin.site.register(BHuesped,AdminBHuesped)
