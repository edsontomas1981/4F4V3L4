from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from Classes.home import Home
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from plataforma.models.Propostas import Propostas

def mostra_propostas(request):
    usuario=request.user
    pedido,imagens, prop_enviadas,propostaRecebidas = Home.gerarHome(usuario.id)
    paginator = Paginator(prop_enviadas, 5) # Mostra 5 por pagina
        
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'./prop_enviadas.html',{'page_obj': page_obj})    

@login_required(login_url='/auth/login/')
def prop_enviadas(request):
    
    if request.method == "GET" :
        return mostra_propostas(request)
    elif request.method == "POST" :
        if 'exclui_proposta' in request.POST:
            proposta=Propostas(id=request.POST.get('id'))
            proposta.delete()
            messages.add_message(request,constants.WARNING,'Proposta excluida !')
            return mostra_propostas(request)
        elif 'altera_proposta' in request.POST:
            proposta=Propostas(id=request.POST.get('id'))
            proposta.delete()
            messages.add_message(request,constants.WARNING,'Proposta Alterada !')
            return mostra_propostas(request)
