from plataforma.models import Categorias, Enderecos, Pedidos
from usuario.models import Usuarios

class Pedido():
    def __init__ (self,categ_escolhida,cep,logradouro,bairro,cidade,uf,numero,titulo,descricao,usuario,imagem):
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
        pedido.imagem=self.imagem
        pedido.pedEndereco=endereco
        pedido.pedCateg=categoria
        pedido.pedUser=self.user
        endereco.save()
        pedido.save()
        
        
    
