from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from f4v3l4 import forms
from . import models
from Classes.salvarPedidos import Pedido

@login_required(login_url='/auth/login/')
def home(request):
    pedidos = models.Pedidos.objects.prefetch_related().all()
    if request.method == "GET" :
        return render(request,'./home.html',{'pedidos' : pedidos })
    elif request.method == "POST" :
        return render(request,'./home.html',{'pedidos' : pedidos})

@login_required(login_url='/auth/login/')
def enviarProposta(request):
    if request.method == "GET" :
        return render(request,'./enviaProposta.html')
    elif request.method == "POST" :
        return render(request,'./enviaProposta.html')

@login_required(login_url='/auth/login/')
def pedidos(request):
    categoria = models.Categorias.objects.all()
    if request.method == "GET" :
        return render(request,'./cadastropedidos.html',{'categoria' : categoria}) #categoria e a chave do dicionário que ira carregar todos os valores
    elif request.method == "POST" :
        return render(request,'./cadastropedidos.html',{'categoria' : categoria})

@login_required(login_url='/auth/login/')
def cadastrarPedido(request):
    if request.method == "GET" :
        return render(request,'./cadastropedidos.html')
    elif request.method == "POST" :
        path_imagem = request.POST.get('path_imagem')
        titulo = request.POST.get('titulo')
        return HttpResponse(titulo)

@login_required
def cadPedidos(request):
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
        imagem=request.POST.get('imagem')
        user = request.user
        pedido=Pedido(categ_escolhida,cep,logradouro,
                      bairro,cidade,uf,numero,titulo,
                      descricao,user,imagem)
        pedido.salvaPedidos()

    return HttpResponse("deu certo")

class ViewFaleConosco(FormView):
    template_name = 'fale.html'
    form_class = forms.FormFaleConosco
    success_url = '/'

class ViewCadPed(FormView):
    template_name = 'cadastropedidos.html'
    form_class = forms.FormCadPed
    success_url = '/'
