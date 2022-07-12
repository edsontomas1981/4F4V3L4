from django import forms
from plataforma.models import Categorias

class FormCadProfissional(forms.Form):
    lista_categoria=Categorias.objects.values_list('categoria',flat=True).order_by('categoria')
    categoria=forms.ModelMultipleChoiceField(lista_categoria,required=True,
    widget=forms.Select(attrs={}))
    titulo_profissional=forms.CharField(required=True,label='Profissão')
    sobre=forms.CharField(required=True,label='Sobre',
    widget=forms.Textarea(attrs={'rows':4}))
