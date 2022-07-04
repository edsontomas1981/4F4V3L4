from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuario.models import Usuarios
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from plataforma import models

def login(request):
     if request.method == "GET" : 
          if request.user.is_authenticated:
               return redirect('/')
          else:
               return render(request,'./login.html')
     elif request.method == 'POST':
          username = request.POST.get('username')
          senha = request.POST.get('senha')
          usuario = auth.authenticate(username=username,password=senha)
          if not usuario:
               messages.add_message(request,constants.ERROR,'Usuário ou senha inválidos')
               return render(request,'./login.html')
          else:
               auth.login(request, usuario)
               return redirect('/')