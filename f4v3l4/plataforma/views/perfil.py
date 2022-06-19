from usuario.models import Contatos as MdlContatos
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from Classes.classes import Contatos
from usuario.models import Usuarios

@login_required(login_url='/auth/login/')
def editarPerfil(request):
    usuario=request.user
   
    if request.method == "GET" :
        contatos=MdlContatos.objects.filter(usuario_fk=usuario)
        return render(request,'./editarperfil.html',{'contatos':contatos})

    elif request.method == 'POST':
        tipo=request.POST.get('tipo')
        vContato=request.POST.get('contato')
        
        if 'incluiContato' in request.POST:
            contato=Contatos(tipo,vContato,usuario)
            contato.salvaContato()
            contatos=MdlContatos.objects.filter(usuario_fk=usuario)
            
            return render (request,'./editarperfil.html',{'contatos':contatos})
        
        elif 'atualiza' in request.POST:
            
            contatos=MdlContatos.objects.filter(usuario_fk=usuario)
            return render(request,'./editarperfil.html',{'contatos':contatos})        
        return render (request,'./editarperfil.html')

@login_required(login_url='/auth/login/')
def mostraPerfil(request):
    if request.method == "GET" :
        return render(request,'./meuperfil.html')
    elif request.method == 'POST':
        return render (request,'./meuperfil.html')

@login_required(login_url='/auth/login/')
def salvaPerfil(request):
    if request.method == "GET" :    
        return render (request,'./meuperfil.html')
    elif request.method == 'POST':
        tabela=request.POST.get('contato')
        return render (request,'./sucesso.html')