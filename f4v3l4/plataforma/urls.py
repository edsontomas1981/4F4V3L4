from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.home,name='home'),
    path('enviarProposta/', views.enviarProposta, name='enviarProposta'),
    path('cadastropedidos/',views.cadPedido,name='cadastro_pedidos'),
    path('faleconosco/', views.ViewFaleConosco.as_view(),name='fale'),
    path('teste/',views.teste,name='teste'),
    

    # path('faleconosco1/',TemplateView.as_view(template_name='fale.html'),name='fale')
]

