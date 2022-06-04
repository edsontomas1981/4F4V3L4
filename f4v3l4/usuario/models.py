from django.contrib.auth.models import AbstractUser 
from django.db import models
from endereco.models import Enderecos,Contatos



class Usuarios(AbstractUser):
    endereco_fk=models.ForeignKey(Enderecos,null=True,default='',on_delete=models.CASCADE)
    contato_fk=models.ForeignKey(Contatos,null=True,default='' ,on_delete=models.CASCADE)
    
    