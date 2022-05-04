from django.db import models
from usuario.models import Usuarios

class Enderecos (models.Model):
    cep=models.CharField(max_length=8,null=True)
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

class Imagem(models.Model):
    imagem=models.ImageField(upload_to='media', blank=True)

class Pedidos (models.Model):
    titulo=models.CharField(max_length=20,null=True)
    descricao=models.CharField(max_length=30)
    pedImagem=models.ManyToManyField(Imagem, blank=True)
    pedEndereco=models.ForeignKey(Enderecos,null=True,on_delete=models.CASCADE)
    pedCateg=models.ForeignKey(Categorias,null=True,on_delete=models.CASCADE)
    pedUser=models.ForeignKey(Usuarios,null=True,on_delete=models.CASCADE)

class Propostas (models.Model):
    prazo=models.IntegerField()
    valor=models.DecimalField(max_digits=2, decimal_places=2)
    observacao=models.CharField(max_length=50)

    
    




    