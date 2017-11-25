from django.contrib import admin
from .models import Tipo
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class AdminTipo(SimpleHistoryAdmin):
	list_display=('nombre','app','color','icono','created_date','modified_date','history')
	search_fields=('nombre',)

admin.site.register(Tipo,AdminTipo)
#admin.site.register(Tipo, SimpleHistoryAdmin)