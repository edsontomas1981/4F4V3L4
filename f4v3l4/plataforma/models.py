from django.db import models
from usuario.models import Usuarios

class Enderecos (models.Model):
    cep=models.CharField(max_length=8,null=False)
    logradouro=models.CharField(max_length=50,null=False)
    numero=models.CharField(max_length=8)
    bairro=models.CharField(max_length=30)
    cidade=models.CharField(max_length=50)
    uf=models.CharField(max_length=2)

class Contatos (models.Model):
    tipo=models.CharField(max_length=15)
    contato=models.CharField(max_length=20)


class Categorias(models.Model):
    categoria=models.CharField(max_length=30)
    

class Servicos (models.Model):
    desc_serv=models.CharField(max_length=20)
    idCategoria =models.ForeignKey(Categorias, null=False, on_delete=models.CASCADE)

class Pedidos (models.Model):
    titulo=models.CharField(max_length=20,null=False)
    descricao=models.CharField(max_length=30)
    endereco_fk=models.ForeignKey(Enderecos,null=False,on_delete=models.CASCADE)
    categoria_fk=models.ForeignKey(Categorias,null=False,on_delete=models.CASCADE)
    usuario_fk=models.ForeignKey(Usuarios,null=False,on_delete=models.CASCADE)

class Imagem(models.Model):
    imagem=models.ImageField(upload_to='media', blank=False)
    pedido_fk=models.ForeignKey(Pedidos,null=False,on_delete=models.CASCADE)
    
class Propostas (models.Model):
    prazo=models.IntegerField()
    valor=models.DecimalField(max_digits=2, decimal_places=2)
    observacao=models.CharField(max_length=50)
    usuario=models.ForeignKey(Usuarios,null=False,on_delete=models.CASCADE)
  