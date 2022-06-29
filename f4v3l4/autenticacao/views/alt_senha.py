from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuario.models import Usuarios
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from plataforma import models

def alt_senha(request):
    if request.method == "GET" :
        token=request.GET.get('token')
        email=request.GET.get('email')
        senha=request.GET.get('senha')
        usuario = Usuarios.objects.filter(token=token).first()
        return render(request,'./trocasenha.html',{'usuario':usuario})

def salva_senha(request):
    if request.method == "POST" :
        token=request.POST.get('token')
        senha=request.POST.get('senha')
        usuario = Usuarios.objects.filter(token=token).first()
        usuario.set_password(senha)
        usuario.token=""
        usuario.save()
        return render(request,'./login.html')

