from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from f4v3l4.forms import FormCadPed,ContatoForm
from f4v3l4 import forms
from . import models
from Classes.classes import Pedido,Home,Propostas
from usuario.models import Usuarios

@login_required(login_url='/auth/login/')
def home(request):
    usuario=request.user
    pedidos,imagens, propostaEnviadaPor,propostaRecebidas = Home.gerarHome(usuario.id)
        
    if request.method == "GET" :
        return render(request,'./home.html',{'pedidos':pedidos,'imagens':imagens,'propostaEnviadaPor':propostaEnviadaPor,'propostaRecebidas':propostaRecebidas})
    elif request.method == "POST" :
        return render(request,'./home.html',{'pedidos':pedidos,'imagens':imagens,'propostaEnviadaPor':propostaEnviadaPor,'propostaRecebidas':propostaRecebidas})

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
    pedidos,imagens = Home.gerarHome()
    if request.method == "GET" :
        return render(request,'./home.html',{'pedidos':pedidos,'imagens':imagens})
    elif request.method == 'POST':
        idPedido=request.POST.get('pedido')
        pedidos=models.Pedidos.objects.filter(id=idPedido)
        imagens=models.Imagem.objects.filter(pedido_fk=idPedido)
        return render (request,'detalhesPedidos.html',{'pedidos':pedidos , 'imagens':imagens})
    
@login_required(login_url='/auth/login/')
def editarPerfil(request):
    if request.method == "GET" :
        return render(request,'./editarperfil.html')
    elif request.method == 'POST':
        return render (request,'./editarperfil.html')

@login_required(login_url='/auth/login/')
def mostraPerfil(request):
    if request.method == "GET" :
        return render(request,'./meuperfil.html')
    elif request.method == 'POST':
        return render (request,'./meuperfil.html')

@login_required(login_url='/auth/login/')
def cadastrar_contato(request):
    form = ContatoForm()
    return render(request, "form.html", {'form':form})

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
        print('**************************')
        print(tabela)
        print('**************************')
        return render (request,'./sucesso.html')


