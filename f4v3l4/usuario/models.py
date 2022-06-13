from django.contrib.auth.models import AbstractUser 
from django.db import models
from endereco.models import Enderecos

class Usuarios(AbstractUser):
    foto_perfil=models.ImageField(upload_to='media/usuarios/',blank=True,null=True)
    endereco_fk=models.ForeignKey(Enderecos,null=True,default='',on_delete=models.CASCADE)

class Contatos (models.Model):
    tipo=models.CharField(max_length=15)
    contato=models.CharField(max_length=50)
    usuario_fk=models.ForeignKey(Usuarios,null=True,default='' ,on_delete=models.CASCADE)




    