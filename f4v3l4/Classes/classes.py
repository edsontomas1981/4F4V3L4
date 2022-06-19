from usuario.models import Usuarios
from plataforma.models import Categorias,Imagem, Pedidos,Propostas as ModelPropostas
from django.core.mail import send_mail
from usuario.models import Contatos as ModelContatos
from endereco.models import Enderecos
from PIL import Image

def redimensionaImagem(img):
    try:

        largura_desejada = 80
        imagem = Image.open(img)

        largura_imagem = imagem.size[0]
        altura_imagem = imagem.size[1]
        percentual_largura = float(largura_desejada) / float(largura_imagem)
        altura_desejada = int((altura_imagem * percentual_largura))
        imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
        imagem.save('imagem-{}x{}.jpeg'.format(imagem.size[0], imagem.size[1]))
        # return imagem
        # return imagem

    except IndexError:
        print('Insira o nome da imagem e 1 inteiro com a largura desejada.')
        print('Exemplo: C:\>python proporcional_img.py imagem.png 300')

class Pedido():
    def __init__ (self,categ_escolhida,cep,logradouro,bairro,
                  cidade,uf,numero,titulo,descricao,usuario,
                  imagem):
        self.categ_escolhida=categ_escolhida
        self.cep=cep
        self.logradouro=logradouro
        self.bairro=bairro
        self.cidade=cidade
        self.uf=uf
        self.numero=numero
        self.titulo=titulo
        self.descricao=descricao
        self.user=usuario
        self.imagem=imagem
    
    def salvaPedidos(self):
        categoria=Categorias.objects.get(categoria=self.categ_escolhida)
        endereco=Enderecos()
        pedido=Pedidos()
        endereco.cep=self.cep
        endereco.logradouro  =self.logradouro
        endereco.numero=self.numero
        endereco.bairro=self.bairro
        endereco.cidade=self.cidade
        endereco.uf=self.uf
        pedido.titulo=self.titulo
        pedido.descricao=self.descricao
        pedido.endereco_fk=endereco
        pedido.categoria_fk=categoria
        pedido.usuario_fk=self.user
        endereco.save()
        pedido.save()
        imagens = self.imagem
        for i in imagens:
            imagem=Imagem()
            imagem.imagem=i
            imagem.pedido_fk=pedido 
            imagem.save() 

    def buscarPedidos(self):
        pedido=Pedidos.object.all()
        print(pedido)
    
class Home():
    def gerarHome(idUsuario):
        #Seleciona todos por enquanto depois ira usar um filtro de pedidos em aberto
        pedidos=Pedidos.objects.all()
        imagens=Imagem.objects.all()
        propostaEnviadaPor=ModelPropostas.objects.filter(usuarioProposta_fk=idUsuario)
        #Selecionar somente propostas ref a pedidos do usuario corrente
        propostasRecebidas=ModelPropostas.objects.all()
        propRec=[x for x in propostasRecebidas if x.pedido_fk.usuario_fk.id==idUsuario]
        return pedidos , imagens , propostaEnviadaPor , propRec
    

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
        for proposta in propostasRejeitadas:
            proposta.propostaAceita=False
            proposta.save()
        mensagem=f'''Olá {proposta.usuarioProposta_fk.first_name}!
        O pedido de {pedido.titulo} foi aceito por {proposta.usuarioProposta_fk.first_name}
        com o valor de R$ {proposta.valor} e o prazo de {proposta.prazo} dias.
        '''
        email=Email('edson.transpioneira@gmail.com','Proposta Aceita',mensagem)
        email.enviarEmail()

class Email():
    
    def __init__(self,destinatario,assunto,mensagem) -> None:
        self.destinatario=destinatario
        self.assunto=assunto
        self.mensagem=mensagem
        
    def enviarEmail(self):
        send_mail(
        self.assunto,
        self.mensagem,
        self.destinatario,
        [self.destinatario],
        fail_silently=False,)

class Mensagem ():
    def __init__(self,remetente,destinatario,assunto,mensagem,data,hora,lido):
        self.remetente=remetente
        self.destinatario=destinatario
        self.assunto=assunto
        self.mensagem=mensagem
        self.data=data
        self.hora=hora
        self.lido=lido

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




