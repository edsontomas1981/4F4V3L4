from django.contrib.auth.models import AbstractUser 
from django.db import models
from plataforma.models import Enderecos , Contatos, Propostas, Trabalhos

class Usuarios(AbstractUser):
    idEndereco = models.ForeignKey(Enderecos, null=True, on_delete=models.CASCADE)
    idContato  = models.ManyToManyField(Contatos)
    idTrabalhos = models.ManyToManyField(Trabalhos)
    idPropostas = models.ManyToManyField(Propostas)
    
    
