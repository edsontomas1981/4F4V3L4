from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.home import Home
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def prop_recebidas(request):
    usuario=request.user
    pedido,imagens, prop_enviadas,prop_recebidas = Home.gerarHome(usuario.id)
    paginator = Paginator(prop_recebidas, 5) # Mostra 5 por pagina
        
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == "GET" :
        return render(request,'./prop_recebidas.html',{'page_obj': page_obj})
    elif request.method == "POST" :
        return render(request,'./prop_recebidas.html',{'page_obj': page_obj})