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
