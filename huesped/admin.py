from django.contrib import admin
from .models import APersona, BHuesped
# Register your models here.

class AdminAPersona(admin.ModelAdmin):
	list_display=('identificacion','tipoIdentificacion','nombres','apellidos','fechaNacimiento','genero',
		'created_by','modified_by')
	search_fields=('nombres','apellidos','identificacion')
	list_filter=('genero','tipoIdentificacion')

class AdminBHuesped(admin.ModelAdmin):
	list_display=('identificacion','persona','fechaEntrada','fechaSalida','acompananteDe',
		'hospedado','habitacion','created_by','modified_by')
	search_fields=('habitacion','persona')
	list_filter=('hospedado', 'fechaEntrada','fechaSalida','created_by')


admin.site.register(APersona,AdminAPersona)
admin.site.register(BHuesped,AdminBHuesped)
