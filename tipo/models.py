from django.db import models
from colorful.fields import RGBColorField
from simple_history.models import HistoricalRecords
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class BaseModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
	modified_date = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='modified_by')

	class Meta:
		abstract = True

@python_2_unicode_compatible
class Tipo(BaseModel):
	nombre = models.CharField(max_length=50)
	app = models.CharField(max_length=50)
	color = RGBColorField(default='#000000')
	icono = models.CharField(max_length=50, null=True, blank=True)
	history = HistoricalRecords()

	def __str__(self):
		return self.nombre

	class Meta:		
		unique_together = [
			["nombre","app"],
		]
		db_table = 'tipo_tipo'
		verbose_name = 'Tipo'

