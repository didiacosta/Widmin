from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.encoding import python_2_unicode_compatible
from tipo.models import Tipo
from django.conf import settings
# Create your models here.

class BaseModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
	modified_date = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
	# created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='infraestructura_created_by')
	# modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='infraestructura_modified_by')

	class Meta:
		abstract = True


@python_2_unicode_compatible
class AequipoControlador(BaseModel):
	nombre = models.CharField(max_length=50)
	ip = models.CharField(max_length=50)
	nombreUsuario = models.CharField(max_length=50)
	clave = models.CharField(max_length=50)
	puerto = models.IntegerField(default=8728)
	history = HistoricalRecords()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='AequipoControlador_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='iAequipoControlador_modified_by')

	def __str__(self):
		return self.nombre

	class Meta:		
		unique_together = [
			["nombre"],
		]
		db_table = 'infraestructura_equipocontrolador'
		verbose_name = 'Equipo controlador'	

@python_2_unicode_compatible
class BGrupoEmpresarial(BaseModel):
	nombre = models.CharField(max_length=150)
	tipo = models.ForeignKey(Tipo , related_name = 'fk_infraestructura_tipo',on_delete=models.PROTECT)
	logo = models.ImageField(upload_to='logos',blank=True, null=True, default='logos/defaultGrupoEmpresarial.jpg')
	equipoControlador = models.ForeignKey(AequipoControlador , 
		related_name = 'fk_grupoEmpresarial_equipoControlador',on_delete=models.PROTECT)
	history = HistoricalRecords()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='BGrupoEmpresarial_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='BGrupoEmpresarial_modified_by')

	def __str__(self):
		return self.nombre

	def logoGrupo(self):
		  return """<img width="100px" height="120px" src="%s" alt="logo del grupo empresarial">""" % self.logo.url

	logoGrupo.allow_tags=True

	class Meta:		
		unique_together = [
			["nombre","tipo"],
		]
		db_table = 'infraestructura_grupoempresarial'
		verbose_name = 'Grupo empresarial'

@python_2_unicode_compatible
class CSede(BaseModel):
	grupoEmpresarial = models.ForeignKey(BGrupoEmpresarial , 
		related_name = 'fk_grupoempresarial_sede',on_delete=models.PROTECT)
	nombre = models.CharField(max_length=150)
	logoPropio = models.BooleanField(default=False)
	logo = models.ImageField(upload_to='logos',blank=True, null=True, default='logos/defaultSede.jpg')
	usuarios = models.ManyToManyField(settings.AUTH_USER_MODEL, 
		related_name='fk_sede_usuarios' , 
		verbose_name='Usuarios que pueden ver esta sede')
	history = HistoricalRecords()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='CSede_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='CSede_modified_by')

	def __str__(self):
		return self.nombre

	def logoSede(self):
		  return """<img width="100px" height="120px" src="%s" alt="logo de la sede">""" % self.logo.url

	class Meta:		
		unique_together = [
			["nombre"],
		]
		db_table = 'infraestructura_sede'
		verbose_name = 'Sede del grupo empresarial'	


@python_2_unicode_compatible
class DHabitacion(BaseModel):
	sede = models.ForeignKey(CSede , related_name = 'fk_habitacion_sede',on_delete=models.PROTECT)
	numero = models.CharField(max_length=50)
	tipo = models.ForeignKey(Tipo , related_name = 'fk_habitacion_tipo',on_delete=models.PROTECT)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='DHabitacion_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='DHabitacion_modified_by')

	def __str__(self):
		return self.sede.nombre + ' >> ' + self.numero

	class Meta:		
		unique_together = [
			["numero"],['sede'],
		]
		db_table = 'infraestructura_habitacion'
		verbose_name = 'habitacion'	