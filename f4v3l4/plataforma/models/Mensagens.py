from django.db import models
from usuario.models import Usuarios

class Mensagens (models.Model):
    mensagem=models.CharField(max_length=50)
    userRem_fk=models.ForeignKey(Usuarios,related_name='remetente',
                                null=False,on_delete=models.CASCADE)
    userDest_fk=models.ForeignKey(Usuarios,related_name='destinatario',
                                null=False,on_delete=models.CASCADE)
    dataenvio=models.DateTimeField(auto_now=False, auto_now_add=False)