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
from Classes.token import Token

def recup_senha(request):
     #carregamento de pedidos para a montagem da home caso esteja logado
     pedidos=models.Pedidos.objects.all()
     imagens=models.Imagem.objects.all()
     if request.user.is_authenticated:
          return render(request,'home.html',{'pedidos':pedidos,'imagens':imagens})
     else:
          return render(request,'./recuperarSenha.html')

def envia_email_html(usuario):
     
     html_message = render_to_string('emailrecuperacao.html', {'token':
     usuario.token})
     message = strip_tags(html_message)
     send_mail(subject="Recuperação de senha", 
               message=message,
               html_message=html_message,
               from_email=settings.EMAIL_HOST_USER, 
               recipient_list=[usuario.email], 
               fail_silently=False,
               )

def envia_email_recup(usuario):# envia token para redefinição de senha
     token=Token.gera_chave()
     usuario.token=token# model com o atributo token para a alteração da senha
     usuario.save()
     mensagem=render_to_string('emailrecuperacao.html',{'token':usuario.token})
     mensagem=strip_tags(mensagem)
     
     envia_email_html(usuario)

def email_recup(request):
     
     if request.method == "GET" :
          return render(request,'./recuperarSenha.html')

     elif request.method == "POST" :
          email=request.POST.get('email')
          usuario=Usuarios.objects.filter(email=email).first()

          if usuario :
               envia_email_recup(usuario)
               return render(request,'./emailenviado.html')
          else:
               messages.add_message(request, messages.ERROR, "Email não cadastrado.")
               return render(request,'./recuperarSenha.html')
          
          

         

    
