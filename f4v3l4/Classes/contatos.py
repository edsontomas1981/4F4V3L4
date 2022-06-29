from usuario.models import Contatos as ModelContatos
from usuario.models import Usuarios

class Contatos():
    
    def __init__ (self,tipo,vContato,usuario):
        self.tipo=tipo
        self.contato=vContato
        self.usuario=usuario
        self.usuario=Usuarios.objects.filter(id=self.usuario.id).get()

    def salvaContato(self):
            contato=ModelContatos()
            contato.contato=self.contato
            contato.tipo=self.tipo
            contato.usuario_fk=self.usuario
            contato.save()
