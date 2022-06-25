from django.shortcuts import render,redirect
from usuario.models import Usuarios
from django.contrib import messages
from django.contrib.messages import constants
from plataforma import models

def cadastro(request):
     pedidos=models.Pedidos.objects.all()
     imagens=models.Imagem.objects.all()
     if request.method == "GET" :
          if request.user.is_authenticated:
               return render(request,'home.html',{'pedidos':pedidos,'imagens':imagens})
          else: 
               return render(request,'./cadastrar.html')
     elif request.method == 'POST':
          username = request.POST.get('nome')
          email = request.POST.get('email')
          senha = request.POST.get('senha')
          conf_senha = request.POST.get('conf_senha')
         
          if len(username.strip())==0 or len(senha.strip())==0 or len(conf_senha.strip())==0:
               messages.add_message(request,constants.ERROR,'Preencha todos os campos')
               return redirect('/auth/cadastro/')
          if senha != conf_senha : 
               messages.add_message(request,constants.ERROR,'Senhas e confirmação de senha não conferem')
               return redirect('/auth/cadastro/')
                        
          user = Usuarios.objects.filter(username=username)
                    
          if user.exists():
               messages.add_message(request,constants.ERROR,'Usuário já cadastrado')
               return redirect('/auth/cadastro/')
          else:
               try:
                    user = Usuarios.objects.create_user(username=username,
                                   email=email,
                                   password=senha,
                                   )
                    user.save()
                    messages.add_message(request,constants.SUCCESS,'Usuário cadastrado com sucesso !')
                    return redirect('/auth/login')
               except:
                    messages.add_message(request,constants.ERROR,'Erro interno')
                    redirect('/auth/cadastro/')