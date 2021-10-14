from rest_framework import viewsets
from api.models import Contato
from api.serializer import ContatoSerializer

class ContatosViewSet(viewsets.ModelViewSet):
	queryset = Contato.objects.all()
	serializer_class = ContatoSerializer




