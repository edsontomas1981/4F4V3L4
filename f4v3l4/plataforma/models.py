from pickle import FALSE
from django.db import models

class Enderecos (models.Model):
    cep = models.CharField(max_length=8,null=FALSE)
    logradouro = models.CharField(max_length=50,null=False)
    numero = models.CharField(max_length=8)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    
class Contatos (models.Model):
    tipo = models.CharField(max_length=15)
    contato = models.CharField(max_length=20)

class Categorias(models.Model):
    categoria = models.CharField(max_length=30)

class Servicos (models.Model):
    desc_serv = models.CharField(max_length=20)
    idCategoria  = models.ForeignKey(Categorias, null=False, on_delete=models.CASCADE)

class Trabalhos (models.Model):
    descricao = models.CharField(max_length=30)

class Propostas (models.Model):
    prazo = models.IntegerField()
    valor = models.DecimalField(max_digits=2, decimal_places=2)
    observacao = models.CharField(max_length=50)

    
    




    