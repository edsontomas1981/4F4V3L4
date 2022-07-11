from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from plataforma import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
     path('',views.home,
         name='home'),
    
     path('pedDisp/',views.pedDisp,
         name='pedDisp'),
     
    path('envia_msg/',views.envia_msg,
        name='envia_msg'),

     path('meus_pedidos/',views.meus_pedidos,
         name='meus_pedidos'),
     
     path('prop_enviadas/',views.prop_enviadas,
         name='prop_enviadas'),     
     
     path('prop_recebidas/',views.prop_recebidas,
         name='prop_recebidas'),  
     
     path('configuracoes/',views.alteraConfig,
         name='alteraConfig'),
     
     path('privacidade/',views.privacidade,
         name='privacidade'),
     
     path('mostraPerfil/', 
         views.mostraPerfil, 
         name='mostraPerfil'),
    
     path('aceitarProposta/', 
         views.aceitarProposta, 
         name='aceitarProposta'),
    
     path('salvaPerfil/', 
         views.salvaPerfil, 
         name='salvaPerfil'),
    
     path('enviarProposta/', 
         views.enviarProposta, 
         name='enviarProposta'),
    
    path('pedido/',
         views.pedidos,
         name='pedido'),
    
    path('cadPedido/',
         views.ViewCadPed.as_view(),
         name='cadPedido'),
    
    path('cPedidos/',
         views.cPedidos,
         name='cPedidos'),
    
    path('editarPerfil/', 
         views.editarPerfil, 
         name='editarPerfil'),
    
    path('detalhesPedidos/',
         views.detalhesPedidos,
         name='detalhesPedidos'),
]
urlpatterns += static(settings.STATIC_URL, 
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)
