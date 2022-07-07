from usuario.models import Usuarios
from plataforma.models import Pedidos,Propostas as ModelPropostas
from django.template.loader import render_to_string
from Classes.email import Email

class Propostas():
    
    def __init__(self,pedido:object,usuario:object,valor,prevInicio,prazo
                 ,observacao):
        self.pedido=pedido
        self.usuario=usuario
        self.valor=valor
        self.prevInicio=prevInicio
        self.prazoTermino=prazo
        self.observacao=observacao
        
    def __repr__(self):
        return "Proposta" 

    def salvaProposta(self):
        proposta=ModelPropostas()
        pedido=Pedidos.objects.filter(id=self.pedido.id).get()
        usuario=Usuarios.objects.filter(id=self.usuario.id).get()
        proposta.prazo=self.prazoTermino
        proposta.valor=self.valor
        proposta.observacao=self.observacao
        proposta.prevInicio=self.prevInicio
        proposta.pedido_fk=pedido
        proposta.usuarioProposta_fk=usuario
        proposta.save()
    
    def aceitaProposta(propostaId):
        proposta=ModelPropostas.objects.filter(id=propostaId).get()
        pedido=proposta.pedido_fk
        proposta.propostaAceita=True
        propostasRejeitadas=ModelPropostas.objects.filter(pedido_fk=pedido).exclude(propostaAceita=True)
        proposta.save()
        # marca como rejeitadas as outras propostas
        for proposta in propostasRejeitadas:
            proposta.propostaAceita=False
            proposta.save()
        # Envia email para o usuario que recebeu a proposta
        html_message=render_to_string('batepapo.html')
        email=Email(proposta.usuarioProposta_fk,proposta.usuarioProposta_fk.email,"Proposta aceita",html_message)
        email.envia_email_html()
        # mensagem=f'''Olá {proposta.usuarioProposta_fk.first_name}!
        # O pedido de {pedido.titulo} foi aceito por {proposta.usuarioProposta_fk.first_name}
        # com o valor de R$ {proposta.valor} e o prazo de {proposta.prazo} dias.
        # '''
        # destinatario=proposta.usuarioProposta_fk.email
        # print('***********************************')
        # print(destinatario)
        # email=Email('edsontomasdev@gmail.com','Proposta Aceita',mensagem)
        # email.enviarEmail()