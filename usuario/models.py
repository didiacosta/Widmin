from django.db import models
from django.conf import settings
from infraestructura.models import BGrupoEmpresarial
# Create your models here.

class BaseModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
	modified_date = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

	class Meta:
		abstract = True

class Usuario(BaseModel):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	telefono=models.CharField(null=True, max_length=100)
	grupoEmpresarial = models.ForeignKey(BGrupoEmpresarial, related_name='GrupoEmpresarial_usuario', null=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Usuario_created_by')
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Usuario_modified_by')

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

	def nombres (self):
		return self.user.first_name

	def apellidos(self):
		return self.user.last_name

	def nombreusuario(self):
		return self.user.username	
