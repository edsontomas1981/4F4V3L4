from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.home,name='home'),
    path('enviarProposta/', views.enviarProposta, name='enviarProposta'),
    path('pedido/',views.pedidos,name='pedido'),
    path('cadPedido/',views.cadPedidos,name='cadPedido'),
    path('faleconosco/', views.ViewFaleConosco.as_view(),name='fale'),
]

