from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('recup_senha/', views.recup_senha, name='recup_senha'),
    path('sair/',views.sair,name='sair')    
]
