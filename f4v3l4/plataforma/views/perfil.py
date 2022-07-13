from usuario.models import Contatos as MdlContatos
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from Classes.contatos import Contatos
from usuario.models import Usuarios
from plataforma.models.Categorias import Categorias
from plataforma.models.Profissional import Profissional 

def carrega_perfil(request):
    usuario=request.user
    contatos=MdlContatos.objects.filter(usuario_fk=usuario)
    categorias=Categorias.objects.all().order_by('categoria')
    profissional=Profissional.objects.filter(usuario_fk=usuario)
    return render(request,'./editarperfil.html',{'contatos':contatos,'categorias':categorias,
                                                     'profissional':profissional})

@login_required(login_url='/auth/login/')
def editarPerfil(request):
    usuario=request.user
   
    if request.method == "GET" :
        return carrega_perfil(request)

    elif request.method == 'POST':
        tipo=request.POST.get('tipo')
        vContato=request.POST.get('contato')
        
        if 'incluiContato' in request.POST:
            contato=Contatos(tipo,vContato,usuario)
            contato.salvaContato()
            messages.add_message(request,constants.SUCCESS,'Contato adicionado com sucesso!')
            return carrega_perfil(request)
        
        elif 'inclui_profissao' in request.POST:
            categoria=Categorias.objects.filter(categoria=request.POST.get('categoria')).get()
            profissional=Profissional(usuario_fk=request.user,
                                  categoria_fk=categoria,
                                  titulo_profissional=request.POST.get('profissao'),
                                  sobre=request.POST.get('sobre')
                                  )
            profissional.save()
            messages.add_message(request,constants.SUCCESS,
            'Perfil profissional cadastrado com sucesso !')
                        
            return carrega_perfil(request)
        
        elif 'salva_perfil' in request.POST:
            nome=request.POST.get('nome')
            sobrenome=request.POST.get('sobrenome')
            usuario.first_name=request.POST.get('nome')
            usuario.last_name=request.POST.get('sobrenome')
            usuario.foto_perfil=request.POST.get('foto_perfil')
            usuario.save()
            return carrega_perfil(request)
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