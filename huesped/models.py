from django.db import models
from infraestructura.models import CSede, DHabitacion
from simple_history.models import HistoricalRecords
from django.utils.encoding import python_2_unicode_compatible
from tipo.models import Tipo
from django.conf import settings
from widminProject import resource
# Create your models here.

class BaseModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
	modified_date = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

	class Meta:
		abstract = True

class APersona(BaseModel):
	generos = ((u'0',u'[Seleccione...]'),(u'1',u'Masculino'),
		(u'2',u'Femenino'),)	
	identificacion = models.IntegerField()
	tipoIdentificacion = models.ForeignKey(Tipo , related_name = 'fk_Persona_tipo',on_delete=models.PROTECT)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	fechaNacimiento = models.DateField()
	genero = models.CharField(max_length=1,choices=generos, default=0)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='APersona_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='APersona_modified_by')
	history = HistoricalRecords()

	def __str__(self):
		return self.nombres + ' ' + self.apellidos

	class Meta:		
		unique_together = [
			["identificacion",'tipoIdentificacion'],
		]
		db_table = 'huesped_persona'
		verbose_name = 'Persona'	

class BHuesped(BaseModel):
	persona = models.ForeignKey(APersona , related_name = 'fk_huesped_Persona',on_delete=models.PROTECT)
	profesionOficio = models.CharField(max_length=50, null=True,blank=True)
	fechaEntrada = models.DateField()
	fechaSalida = models.DateField()
	acompananteDe = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
	habitacion = models.IntegerField()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='BHuesped_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='BHuesped_modified_by')
	history = HistoricalRecords()

	def __str__(self):
		return self.persona.nombres + ' ' + self.persona.apellidos

	def identificacion(self):
		return self.persona.identificacion

	def save(self):
		#conexion al microtick
		crearUsuario(self.persona.identificacion,self.persona.identificacion)
		pass

	class Meta:
		db_table = 'huesped_huesped'
		verbose_name = 'Huesped'
