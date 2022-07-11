from django.shortcuts import render,redirect
from Classes.mensagem import Mensagem

def envia_msg(request):
    msg=Mensagem(request.POST['remetente'],request.POST['destinatario'],request.POST['mensagem'])
    msg.enviar_mensagem()
    return redirect('/')
    
                 
    
    
    