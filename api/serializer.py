from rest_framework import serializers
from api.models import Contato

class ContatoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contato
		fields = ['id', 'nome', 'email', 'telefone', ]#'mensagem']
