from django.db import models

class Categorias(models.Model):
    categoria=models.CharField(max_length=30)