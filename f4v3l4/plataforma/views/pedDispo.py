from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.classes import Home
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_sameorigin
@login_required(login_url='/auth/login/')
def pedDisp(request):  
    usuario=request.user
    pedidos,imagens, propostaEnviadaPor,propostaRecebidas = Home.gerarHome(usuario.id)
    if request.method == "GET" :
        return render(request,'./pedDisp.html',{'pedidos':pedidos,
                        'imagens':imagens,'propostaEnviadaPor':propostaEnviadaPor,
                        'propostaRecebidas':propostaRecebidas})
    elif request.method == "POST" :
        return render(request,'./pedDisp.html',{'pedidos':pedidos,'imagens':imagens,
                        'propostaEnviadaPor':propostaEnviadaPor,
                        'propostaRecebidas':propostaRecebidas})
