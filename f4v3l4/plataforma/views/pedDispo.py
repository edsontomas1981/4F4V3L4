from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.home import Home
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='/auth/login/')
def pedDisp(request):  
    usuario=request.user
    pedido,imagens, propostaEnviadaPor,propostaRecebidas = Home.gerarHome(usuario.id)
    paginator = Paginator(pedido, 5) # Mostra 5 por pagina
      
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "GET" :
        return render(request,'./pedDisp.html',{'page_obj':page_obj})
    elif request.method == "POST" :
        return render(request,'./pedDisp.html',{'page_obj':page_obj})
