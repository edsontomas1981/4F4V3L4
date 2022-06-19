from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.classes import Home
from django.contrib.auth.decorators import login_required

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
