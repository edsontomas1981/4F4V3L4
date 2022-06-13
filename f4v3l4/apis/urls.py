from django.urls import path
from . import views

urlpatterns = [
    path('mensagens/', views.Mensagem.as_view(), name='mensagens'),
    path('contatos/',views.Contato.as_view(),name='contatos'),
]
