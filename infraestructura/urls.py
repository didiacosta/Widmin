from django.conf.urls import url

from .views import SedeListView

urlpatterns = [
    url(r'^sedes/$', SedeListView.as_view(), name='infraestructura.sedes'),
    # url(r'^crearCertificado/$', CertificadoCreateView.as_view(), name='certificado.certificado-crear'),
    # url(r'^editarCertificado/(?P<pk>[\w\-]+)/$', CertificadoUpdateView.as_view(), name='certificado.certificado-editar'),
    # url(r'^borrarCertificado/(?P<pk>[\w\-]+)/$', CertificadoDeleteView.as_view(), name='certificado.certificado-borrar'),
    # url(r'^detalleCertificado/(?P<pk>[\w\-]+)/$', CertificadoDetailView.as_view(), name='certificado.certificado-detalle'),
    # url(r'^detalleCertificadoPublic/(?P<pk>[\w\-]+)/$', CertificadoPublicDetailView.as_view(), name='certificado.certificado-detalle-public'),


 
]