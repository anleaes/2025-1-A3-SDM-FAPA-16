"""
URL configuration for rentcar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('veiculos/', include('veiculos.urls', namespace='veiculos')),
    path('reservas/', include('reservas.urls', namespace='reservas')),
    path('acessorios/', include('acessorios.urls', namespace='acessorios')),
    path('itemreserva/', include('itemreserva.urls', namespace='itemreserva')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
    path('veiculoacessorio/', include('veiculoacessorio.urls', namespace='veiculoacessorio')),
]
