from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.classes import Pedido,Home
from django.contrib.auth.decorators import login_required
from plataforma import models
from django.contrib.messages import constants
from django.contrib import messages
from django.views.generic.edit import FormView
from f4v3l4.forms import FormCadPed

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

class ViewCadPed(FormView):
    template_name = 'cadastropedidos.html'
    form_class = FormCadPed
    success_url = '/'