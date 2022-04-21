from curses.ascii import HT
from django.shortcuts import render,redirect
from django.http import HttpResponse

def cadastro(request):
     if request.method == "GET" : 
          return render(request,'./cadastrar.html')
     elif request.method == 'POST':
          if 'cadastro' in request.POST :
               username = request.POST.get('nome')
               email = request.POST.get('email')
               senha = request.POST.get('senha')
               sobrenome = request.POST.get('senha')
               conf_senha = request.POST.get('conf_senha')
               print(request.POST)
               return HttpResponse('Cadastro')
          elif 'teste' in request.POST :
               return HttpResponse('teste')
          

def login(request):
     return render(request,'./logar.html')

def recup_senha(request):
     return render(request,'./recuperarSenha.html')
