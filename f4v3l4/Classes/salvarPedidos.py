from email.mime import image
from plataforma.models import Categorias, Enderecos, Imagem, Pedidos
from usuario.models import Usuarios

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
    
        
    
