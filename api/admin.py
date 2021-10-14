from django.contrib import admin
from api.models import Contato

class Contatos(admin.ModelAdmin):
	list_display = ('id', 'nome', 'email', 'telefone')
	list_display_links = ('id', 'nome')
	search_fields =('nome', )

admin.site.register(Contato, Contatos)


