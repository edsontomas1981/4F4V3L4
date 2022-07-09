from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Classes.home import Home
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def home(request):
    usuario=request.user
    pedido,imagens, propostaEnviadaPor,propostaRecebidas = Home.gerarHome(usuario.id)
    paginator = Paginator(pedido, 5) # Mostra 5 por pagina
    paginator_prop_env=Paginator(propostaEnviadaPor,5)
        
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj_prop_rec = paginator_prop_env.get_page(page_number)
    
    
    if request.method == "GET" :
        return render(request,'./home.html',{'page_obj': page_obj,'page_obj_prop_rec': page_obj_prop_rec,
                                            'imagens':imagens,'propostaRecebidas':propostaRecebidas})
    elif request.method == "POST" :
        return render(request,'./home.html',{'page_obj': page_obj,'pedido':pedido,
                                            'imagens':imagens,'propostaEnviadaPor':propostaEnviadaPor,
                                            'propostaRecebidas':propostaRecebidas})
