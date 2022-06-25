import email
from django.shortcuts import render,redirect    
from django.http import HttpResponse
from usuario.models import Usuarios
from django.contrib import messages
from django.contrib.messages import constants
from plataforma import models
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib
from Classes import classes

def recup_senha(request):
     #carregamento de pedidos para a montagem da home caso esteja logado
     pedidos=models.Pedidos.objects.all()
     imagens=models.Imagem.objects.all()
     if request.user.is_authenticated:
          return render(request,'home.html',{'pedidos':pedidos,'imagens':imagens})
     else:
          return render(request,'./recuperarSenha.html')

def envia_email_recup(usuario):# envia token para redefinição de senha
    
     usuario.token = hashlib.sha256().hexdigest() #model com o atributo token para a alteração da senha
     usuario.save()
     assunto="Redefinição de Senha."
     mensagem=render_to_string('recuperacao.html',{'token':usuario.token})
     mensagem=strip_tags(mensagem)
     email=classes.Email(usuario.email,assunto,mensagem)
     email.enviarEmail()     


def email_recup(request):
     if request.method == "GET" :
          return render(request,'./recuperarSenha.html')

     elif request.method == "POST" :
          email=request.POST.get('email')
          usuario=Usuarios.objects.filter(email=email).first()
          if usuario :
               envia_email_recup(usuario)
               messages.add_message(request,constants.SUCCESS,'Email foi enviado com sucesso')
               return render(request,'./recuperarSenha.html')
          else:
               messages.add_message(request,constants.ERROR,'Email Inválido')
               return render(request,'./recuperarSenha.html')
         

    
