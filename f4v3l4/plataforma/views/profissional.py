from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from f4v3l4.forms.form_cad_profissional import FormCadProfissional
from django.contrib.messages import constants
from django.contrib import messages
from plataforma.models import Profissional,Categorias

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

class ViewCadProfissional(FormView):
    template_name = 'cad_profissional.html'
    form_class = FormCadProfissional
    success_url = '/'