from django import forms
from plataforma.models import Contatos,Categorias

class FormFaleConosco(forms.Form):
    nome = forms.CharField(required=True)
    email_origem = forms.EmailField(required=True,label='Entre com seu email')
    mensagem = forms.CharField(required=True ,widget=forms.Textarea)
    teste = forms.CharField(required=True)

class FormCadPed(forms.Form):
    categ = Categorias.objects.values_list('categoria',flat=True)
    categoria = forms.ModelMultipleChoiceField(categ,widget=forms.Select(attrs={}))
    titulo = forms.CharField(required=True,label='Título')
    descricao = forms.CharField(required=True,label='Descrição')
    imagem = forms.ImageField(widget=forms.FileInput(attrs={
    'class': 'btn btn-secondary'}))
    data_pedido = forms.DateField(required=True,label='Data pedido')
    data_entrega = forms.DateField(required=True,label='Data entrega')
    cep=forms.CharField(widget=forms.TextInput(attrs={
    'onblur':'pesquisacep(this.value);','name': 'cep'}))
    rua = forms.CharField(widget=forms.TextInput(attrs={
    'name':"rua", 'id':"rua"}))
    bairro = forms.CharField(widget=forms.TextInput(attrs={
    'name':'bairro','id':"bairro"}))
    cidade=forms.CharField(widget=forms.TextInput(attrs={
    'name':'cidade','id':"cidade"}))
    estado = forms.CharField(widget=forms.TextInput(attrs={
    'name':'uf','id':"uf"}))
    numero=forms.CharField(required=True,label='Nº')
    complemento=forms.CharField(required=True,label='Complemento')

class ContatoForm (forms.ModelForm):
    class Meta:
        model=Contatos
        fields=['tipo','contato']
