from django import forms
from plataforma.models import Categorias,Propostas

class FormFaleConosco(forms.Form):
    nome = forms.CharField(required=True)
    email_origem = forms.EmailField(required=True,label='Entre com seu email')
    mensagem = forms.CharField(required=True ,widget=forms.Textarea)
    teste = forms.CharField(required=True)

class FormCadPed(forms.Form):
    categ = Categorias.objects.values_list('categoria',flat=True)
    categoria = forms.ModelMultipleChoiceField(categ,required=True,
    widget=forms.Select(attrs={}))
    titulo = forms.CharField(required=True,label='Título')
    descricao = forms.CharField(required=True,label='Descrição',
    widget=forms.Textarea(attrs={'rows':2}))
    imagem = forms.ImageField(widget=forms.ClearableFileInput(attrs={
    'class': 'btn btn-secondary','multiple':True }))
    cep=forms.CharField(widget=forms.TextInput(attrs={
    'onblur':'pesquisacep(this.value);','name': 'cep'}))
    rua = forms.CharField(widget=forms.TextInput(attrs={
    'name':"rua", 'id':"rua"}))
    numero=forms.CharField(required=True,label='Nº')
    complemento=forms.CharField(label='Complemento')
    bairro = forms.CharField(widget=forms.TextInput(attrs={
    'name':'bairro','id':"bairro"}))
    cidade=forms.CharField(widget=forms.TextInput(attrs={
    'name':'cidade','id':"cidade"}))
    uf = forms.CharField(widget=forms.TextInput(attrs={
    'name':'uf','id':"uf"}))


