from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from f4v3l4 import forms
from . import models
from Classes.salvarPedidos import Pedido
from f4v3l4.forms import FormCadPed,ContatoForm

@login_required(login_url='/auth/login/')
def home(request):
    pedidos = models.Pedidos.objects.all()
    imagens = set()
    for pedido in pedidos:
        imagens.add(pedido.pedImagem.all())
    if request.method == "GET" :
        return render(request,'./home.html',{'pedidos' : pedidos,'imagens':imagens })
    elif request.method == "POST" :
        return render(request,'./home.html',{'pedidos' : pedidos,'imagens':imagens})

@login_required(login_url='/auth/login/')
def enviarProposta(request):
    if request.method == "GET" :
        return render(request,'./enviaProposta.html')
    elif request.method == "POST" :
        return render(request,'./enviaProposta.html')

@login_required(login_url='/auth/login/')
def pedidos(request):
    categoria = models.Categorias.objects.values('categoria')
    if request.method == "GET" :
        return render(request,'./cadastropedidos.html',
        {'categoria' : categoria}) #categoria e a chave do dicionário que ira carregar todos os valores
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

@login_required
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
        imagem=request.FILES.get('imagem')
        user = request.user
        pedido=Pedido(categ_escolhida,cep,logradouro,
                      bairro,cidade,uf,numero,titulo,
                      descricao,user,imagem)
        pedido.salvaPedidos()
        messages.add_message(request,constants.SUCCESS,
        'Pedido cadastrado com sucesso !')
        return redirect('/cadPedido/')

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
