from usuario.models import Usuarios
from plataforma.models import Categorias, Enderecos, Imagem, Pedidos,Propostas as ModelPropostas

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
    def gerarHome():
        pedidos=Pedidos.objects.all()
        imagens=Imagem.objects.all()
        return pedidos , imagens

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
