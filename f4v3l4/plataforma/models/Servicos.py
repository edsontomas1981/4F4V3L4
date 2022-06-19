from django.db import models
from .Categorias import Categorias

class Servicos (models.Model):
    desc_serv=models.CharField(max_length=20)
    idCategoria =models.ForeignKey(Categorias, null=False, on_delete=models.CASCADE)