from django.shortcuts import render,redirect
from usuario.models import Usuarios
from django.contrib import messages
from django.contrib.messages import constants
from Classes.senha import Senha

def alt_senha(request):
    if request.method == "GET" :
        token=request.GET.get('token')
        usuario = Usuarios.objects.filter(token=token).first()
        return render(request,'./trocasenha.html',{'usuario':usuario})
        
def salva_senha(request):
    if request.method == "POST" :
        token=request.POST.get('token')
        senha=request.POST.get('senha')
        senha_confirm=request.POST.get('senha_confirm')
        usuario = Usuarios.objects.filter(token=token).first()
        if usuario.token=='' or token=='' or usuario.token==None : #verifica se o token veio na requisição e se ele é válido
            messages.add_message(request,constants.ERROR,'Token inválido')
            return redirect('/auth/recup_senha/')
        else:
            senha_e_valida,msg_erro=Senha.valida_senha(senha,senha_confirm)
            if senha_e_valida is True:
                usuario.set_password(senha)
                usuario.token=""
                usuario.save()
                messages.add_message(request,constants.SUCCESS,'Senha alterada com sucesso !')
                return redirect('/auth/login/',{'usuario':usuario})
            else:
                messages.add_message(request,constants.ERROR,msg_erro)
                usuario = Usuarios.objects.filter(token=token).first()
                redirecionamento='/auth/alt_senha/?token='+usuario.token
                return redirect(redirecionamento,{'usuario':usuario})
    elif request.method == "GET" :
        return redirect('/auth/recup_senha/')
        
        
        
        

