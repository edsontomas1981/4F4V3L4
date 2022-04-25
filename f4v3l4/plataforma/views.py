from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from f4v3l4 import forms
# Create your views here.

@login_required(login_url='/auth/login/')
def home(request):
    if request.method == "GET" : 
        return render(request,'./home.html')
    elif request.method == "POST" :
        return render(request,'./home.html')

@login_required(login_url='/auth/login/')
def enviarProposta(request):
    if request.method == "GET" : 
        return render(request,'./enviaProposta.html')
    elif request.method == "POST" :
        return render(request,'./enviaProposta.html')

@login_required(login_url='/auth/login/')
def cadPedido(request):
    if request.method == "GET" : 
        return render(request,'./cadastropedidos.html')
    elif request.method == "POST" :
        return render(request,'./cadastropedidos.html')


class ViewFaleConosco(FormView):
    template_name = 'fale.html'
    form_class = forms.FormFaleConosco
    success_url = '/'

class ViewCadPed(FormView):
    template_name = 'cadastropedidos.html'
    form_class = forms.FormCadPed
    success_url = '/'
    