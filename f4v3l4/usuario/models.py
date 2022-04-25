from django.contrib.auth.models import AbstractUser 
from django.db import models

class Usuarios(AbstractUser):
    bio = models.TextField(blank=True)
    cadastrar = models.TimeField