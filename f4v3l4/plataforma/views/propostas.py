from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.classes import Propostas
from django.contrib.auth.decorators import login_required
from plataforma import models

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