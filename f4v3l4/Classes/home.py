from plataforma.models import Imagem, Pedidos,Propostas as ModelPropostas

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