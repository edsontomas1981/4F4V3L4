from black import Mode
from django.db import models
from plataforma.models import Categorias
from usuario.models import Usuarios

class Profissional (models.Model):
    usuario_fk=models.ForeignKey(Usuarios,null=False,on_delete=models.CASCADE)
    categoria_fk=models.ForeignKey(Categorias,null=False,on_delete=models.CASCADE)
    titulo_profissional=models.CharField(max_length=20,null=False)
    sobre=models.CharField(max_length=50)
    
    
    
