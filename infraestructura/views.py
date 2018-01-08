from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import CSede
from usuario.models import Usuario

class SedeListView(ListView):
	model = CSede
	template_name = 'infraestructura/listasedes.html'
	paginate= 10

	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)

		if self.request.GET.get('textoBusqueda'):
			queryset = self.model.objects.filter(nombre__icontains=self.request.GET.get('textoBusqueda'),
				grupoEmpresarial=usuario.grupoEmpresarial)
		else:
			queryset = self.model.objects.filter(grupoEmpresarial=usuario.grupoEmpresarial)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(SedeListView, self).get_context_data(**kwargs)
		if not context.get('is_paginated', False):
			return context

		paginator = context.get('paginator')
		num_pages = paginator.num_pages
		current_page = context.get('page_obj')
		page_no = current_page.number

		if num_pages <= 17 or page_no <= 9:  # case 1 and 2
		    pages = [x for x in range(1, min(num_pages + 1, 18))]
		elif page_no > num_pages - 9:  # case 4
			pages = [x for x in range(num_pages - 16, num_pages + 1)]
		else:  # case 3
			pages = [x for x in range(page_no - 7, page_no + 8)]

		context.update({'pages': pages})
		return context
