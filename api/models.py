from django.db import models

class Contato(models.Model):
	nome = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	telefone = models.CharField(max_length = 15)

	def __str__(self):
		return self.nome

