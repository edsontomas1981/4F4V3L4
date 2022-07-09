from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Classes.home import Home
from plataforma.models import Pedidos
def meus_pedidos (request) :
    usuario=request.user
    pedido=Pedidos.objects.filter(usuario_fk=usuario)        
    paginator = Paginator(pedido, 5) # Mostra 5 por pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "GET" :
        return render(request,'./meus_pedidos.html',{'page_obj':page_obj})
    elif request.method == "POST" :
        return render(request,'./meus_pedidos.html',{'page_obj':page_obj})
    