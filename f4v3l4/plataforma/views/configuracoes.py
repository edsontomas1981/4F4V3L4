from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from plataforma.models.Categorias import Categorias

@login_required(login_url='/auth/login/')
def alteraConfig(request):
    if request.method == "GET" :
        return render(request,'./configuracoes.html')
    elif request.method == "POST" :
        categoria=Categorias()
        categoria.categoria=uf=request.POST.get('categoria')
        categoria.save()
        return render(request,'./configuracoes.html')
