from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',views.home,name='home'),
    path('mostraPerfil/', views.mostraPerfil, name='mostraPerfil'),
    path('enviarProposta/', views.enviarProposta, name='enviarProposta'),
    path('pedido/',views.pedidos,name='pedido'),
    path('cadastrarPedido/',views.cadastrarPedido,name='cadastrarPedido'),
    path('cadPedido/',views.ViewCadPed.as_view(),name='cadPedido'),
    path('cPedidos/',views.cPedidos,name='cPedidos'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
    path('detalhesPedidos/',views.detalhesPedidos,name='detalhesPedidos'),
    path('contato/',views.cadastrar_contato,name='contato'),
    path('faleconosco/', views.ViewFaleConosco.as_view(),name='fale'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
