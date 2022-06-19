from django.db import models
from datetime import datetime
from usuario.models import Usuarios
from .Pedidos import Pedidos

class Propostas (models.Model):
    prazo=models.IntegerField()
    valor=models.DecimalField(max_digits=10, decimal_places=2)
    observacao=models.CharField(max_length=50,null=True)
    prevInicio=models.DateField(default=datetime.now)
    usuarioProposta_fk=models.ForeignKey(Usuarios,default='',related_name='usuarioProposta_fk',
                                        null=False,on_delete=models.CASCADE)
    pedido_fk=models.ForeignKey(Pedidos,default='',related_name='pedido_fk',
                                null=False,on_delete=models.CASCADE)
    propostaAceita=models.BooleanField(null=True)