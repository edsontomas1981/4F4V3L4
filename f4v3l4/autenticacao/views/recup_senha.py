from django.shortcuts import render,redirect    
from usuario.models import Usuarios
from django.contrib import messages
from plataforma import models
from django.template.loader import render_to_string
from Classes.token import Token
from Classes.email import Email

def recup_senha(request):
     if request.user.is_authenticated:
          return redirect('/')
     else:
          return render(request,'./recuperarSenha.html')

def envia_email_recup(usuario):# envia token para redefinição de senha
     token=Token.gera_chave()
     usuario.token=token# model com o atributo token para a alteração da senha
     usuario.save()
     html_message=render_to_string('emailrecuperacao.html', {'token':
     usuario.token})
     email=Email(usuario,usuario.email,"Recuperação de senha",html_message)
     email.envia_email_html()

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
