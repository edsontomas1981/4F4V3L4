from plataforma.models.Mensagens import Mensagens
from usuario.models import Usuarios
from datetime import datetime

class Mensagem ():
    def __init__(self,remetente,destinatario,mensagem):
        self.remetente=remetente
        self.destinatario=destinatario
        self.mensagem=mensagem
        self.assunto=''
        self.data=''
        self.hora=''
        self.lido=''
    
    def enviar_mensagem(self):
        remetente=Usuarios.objects.get(id=self.remetente)
        destinatario=Usuarios.objects.get(id=self.destinatario)
        data_e_hora=datetime.now()
        mensagem=Mensagens(userRem_fk=remetente,
                           userDest_fk=destinatario,
                           mensagem=self.mensagem,
                           dataenvio=data_e_hora)
        mensagem.save()
        
    