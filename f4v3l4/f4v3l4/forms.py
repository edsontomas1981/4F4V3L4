from django import forms

class FormFaleConosco(forms.Form):
    nome = forms.CharField(required=True)
    email_origem = forms.EmailField(required=True,label='Entre com seu email')
    mensagem = forms.CharField(required=True ,widget=forms.Textarea)
    teste = forms.CharField(required=True)

class FormCadPed(forms.Form):
    titulo = forms.CharField(required=True,label='Título')
    descricao = forms.CharField(required=True,label='Descrição')
    categoria = forms.CharField(required=True,label='Categoria')
    imagem = forms.ImageField(required=False)
    data_pedido = forms.DateField(required=True,label='Data pedido')
    data_entrega = forms.DateField(required=True,label='Data entrega')
    cep=forms.CharField(required=True,label='Cep')
    rua = forms.CharField(required=True,label='Rua')
    bairro = forms.CharField(required=True,label='Bairro')
    cidade=forms.CharField(required=True,label='Cidade')
    estado = forms.CharField(required=True,label='UF')
    


