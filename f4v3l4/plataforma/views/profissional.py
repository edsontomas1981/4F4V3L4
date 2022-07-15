from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from f4v3l4.forms.form_cad_profissional import FormCadProfissional
from django.contrib.messages import constants
from django.contrib import messages
from plataforma.models import Profissional,Categorias
from django.core.paginator import Paginator

def cad_profissional(request):
    if request.method == "GET" :
        return redirect('/profissional/')
    elif request.method == "POST" :
        categoria=Categorias.objects.filter(categoria=request.POST.get('categoria')).get()
        profissional=Profissional(usuario_fk=request.user,
                                  categoria_fk=categoria,
                                  titulo_profissional=request.POST.get('titulo_profissional'),
                                  sobre=request.POST.get('sobre')
                                  )
        profissional.save()
        messages.add_message(request,constants.SUCCESS,
        'Perfil profissional cadastrado com sucesso !')
        return redirect('/profissional/')

def mostra_lista_profissionais(request,categorias,profissionais):

    paginator = Paginator(profissionais, 5) # Mostra 5 por pagina
        
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    
    return render(request,'./lista_profissionais.html',
                {'page_obj':page_obj,'categorias':categorias})
     

def lista_profissionais (request):
    if request.method == "GET" :
        profissionais=Profissional.objects.all()
        categorias=Categorias.objects.all().order_by('categoria')
        return mostra_lista_profissionais(request,categorias,profissionais)
    
    if request.method == "POST" :
        if 'buscar' in request.POST:
 
            categorias=Categorias.objects.all().order_by('categoria')
            filtro_categorias=Categorias.objects.filter(categoria=request.POST.get('categoria')).get()
            profissionais=Profissional.objects.filter(categoria_fk=filtro_categorias.id)
             
            return mostra_lista_profissionais(request,categorias,profissionais)

class ViewCadProfissional(FormView):
    template_name = 'cad_profissional.html'
    form_class = FormCadProfissional
    success_url = '/'