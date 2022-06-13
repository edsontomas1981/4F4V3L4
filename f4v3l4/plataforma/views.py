from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from f4v3l4.forms import FormCadPed
from f4v3l4 import forms
from . import models
from Classes.classes import Pedido,Home,Propostas
from usuario.models import Usuarios
from rest_framework.views import APIView
from rest_framework.response import Response
from plataforma.models import Mensagens
from usuario.models import Contatos
from apis.serializers import MensagensSerializer, ContatosSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 


@login_required(login_url='/auth/login/')
def home(request):
    usuario=request.user
    pedidos,imagens, propostaEnviadaPor,propostaRecebidas = Home.gerarHome(usuario.id)
    if request.method == "GET" :
        return render(request,'./home.html',{'pedidos':pedidos,
                        'imagens':imagens,'propostaEnviadaPor':propostaEnviadaPor,
                        'propostaRecebidas':propostaRecebidas})
    elif request.method == "POST" :
        return render(request,'./home.html',{'pedidos':pedidos,'imagens':imagens,
                        'propostaEnviadaPor':propostaEnviadaPor,
                        'propostaRecebidas':propostaRecebidas})

@login_required(login_url='/auth/login/')
def aceitarProposta(request):
    usuario=request.user

    if request.method == "GET" :
        return render(request,'./home.html')
    elif request.method == "POST" :
        propostaId=request.POST.get('propostaId')
        proposta=Propostas.aceitaProposta(propostaId)
        return render(request,'./home.html')

@login_required(login_url='/auth/login/')
def enviarProposta(request):
    if request.method == "GET" :
        return render(request,'./erro.html')    
    elif request.method == "POST" :
        usuario=request.user
        valor= request.POST.get('valor').replace('.','')
        valor= valor.replace(',','.')
        observacao= request.POST.get('observacao')
        prevInicio =request.POST.get('prevInicio')
        prazoTermino =request.POST.get('prazoTermino')
        idPedido=request.POST.get('pedido')
        pedido=models.Pedidos.objects.filter(id=idPedido).get()
        proposta=Propostas(pedido,usuario,valor,prevInicio,prazoTermino,observacao)
        proposta.salvaProposta()
        return render(request,'./sucesso.html')

@login_required(login_url='/auth/login/')
def pedidos(request):
    categoria = models.Categorias.objects.values('categoria')
    if request.method == "GET" :
        return render(request,'./cadastropedidos.html',
        {'categoria' : categoria}) 
    elif request.method == "POST" :
        return render(request,'./cadastropedidos.html',
        {'categoria' : categoria})

@login_required(login_url='/auth/login/')
def cadastrarPedido(request):
    if request.method == "GET" :
        return render(request,'./cadastropedidos.html')
    elif request.method == "POST" :
        formulario = FormCadPed(request.POST)
        return HttpResponse(formulario)

@login_required(login_url='/auth/login/')
def cPedidos(request):
    if request.method == "GET" :
            return render(request,'./cadastropedidos.html')
    elif request.method == "POST" :
        categ_escolhida= request.POST.get('categoria')
        cep=request.POST.get('cep')
        logradouro=request.POST.get('rua')
        bairro=request.POST.get('bairro')
        cidade=request.POST.get('cidade')
        uf=request.POST.get('uf')
        numero=request.POST.get('numero')
        titulo=request.POST.get('titulo')
        descricao=request.POST.get('descricao')
        user = request.user
        imagens=request.FILES.getlist('imagem')
        pedido=Pedido(categ_escolhida,cep,logradouro,
                      bairro,cidade,uf,numero,titulo,
                      descricao,user,imagens)
        pedido.salvaPedidos()
        messages.add_message(request,constants.SUCCESS,
        'Pedido cadastrado com sucesso !')
        return redirect('/cadPedido/')

@login_required(login_url='/auth/login/')
def detalhesPedidos(request):
    usuario=request.user
    pedidos,imagens, propostaEnviadaPor,propostaRecebidas = Home.gerarHome(usuario.id)
    if request.method == "GET" :
        return render(request,'./home.html',{'pedidos':pedidos,
                        'imagens':imagens,'propostaEnviadaPor':propostaEnviadaPor,
                        'propostaRecebidas':propostaRecebidas})
    elif request.method == 'POST':
        idPedido=request.POST.get('pedido')
        pedidos=models.Pedidos.objects.filter(id=idPedido)
        imagens=models.Imagem.objects.filter(pedido_fk=idPedido)
        return render (request,'detalhesPedidos.html',{'pedidos':pedidos , 'imagens':imagens})
    
@login_required(login_url='/auth/login/')
def editarPerfil(request):
    if request.method == "GET" :
        tipo=request.GET.get('tipo')
        contato=request.GET.get('contato')    
        print("********GET**********")
        print(request)
        return render(request,'./editarperfil.html')
    elif request.method == 'POST':
        tipo=request.POST.get('tipo')
        contato=request.POST.get('contato') 
        if 'incluiContato' in request.POST:    
            print("********POST**********")
            print('OPA AI SIM')
            return render (request,'./editarperfil.html')
        return render (request,'./editarperfil.html')

@login_required(login_url='/auth/login/')
def mostraPerfil(request):
    if request.method == "GET" :
        return render(request,'./meuperfil.html')
    elif request.method == 'POST':
        return render (request,'./meuperfil.html')

class ViewFaleConosco(FormView):
    template_name = 'fale.html'
    form_class = forms.FormFaleConosco
    success_url = '/'
    

class ViewCadPed(FormView):
    template_name = 'cadastropedidos.html'
    form_class = forms.FormCadPed
    success_url = '/'

@login_required(login_url='/auth/login/')
def salvaPerfil(request):
    if request.method == "GET" :    
        return render (request,'./meuperfil.html')
    elif request.method == 'POST':
        tabela=request.POST.get('contato')
        return render (request,'./sucesso.html')

def batePapo(request):
    if request.method == "GET" :
        return render(request,'./batepapo.html')
    elif request.method == 'POST':
        return render (request,'./batepapo.html')

@api_view()
class Mensagem(APIView):
    def get(self, request):
        mensagens = Mensagens.objects.all()
        serializer = MensagensSerializer(mensagens, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MensagensSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
class Contato(APIView):

    def get(self, request):
        contatos = Contatos.objects.all()
        serializer = ContatosSerializer(contatos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ContatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


