from django.db import models
from .Categorias import Categorias
from endereco.models import Enderecos
from usuario.models import Usuarios

class Pedidos (models.Model):
    titulo=models.CharField(max_length=20,null=False)
    descricao=models.CharField(max_length=30)
    endereco_fk=models.ForeignKey(Enderecos,null=False,on_delete=models.CASCADE)
    categoria_fk=models.ForeignKey(Categorias,null=False,on_delete=models.CASCADE)
    usuario_fk=models.ForeignKey(Usuarios,null=False,on_delete=models.CASCADE)