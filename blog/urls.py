from django import views
#from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from publicacion.models import Publicacion
import cuenta.views, publicacion.views

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls), # sitio de administración

    path('', publicacion.views.index, name='index'), # inicio de la web
    path('nosotros', publicacion.views.nosotros, name='nosotros'), # inicio de la web

    path('blog/post/nueva/', publicacion.views.nueva, name='publicacion_nueva'),
    path('blog/post/editar/<int:id>', publicacion.views.editar, name='publicacion_editar'),
    path('blog/post/eliminar/<int:id>', publicacion.views.eliminar, name='publicacion_eliminar'),
    path('blog/post/<int:id>/', publicacion.views.ver, name='publicacion_ver'),

    path('cuenta/', cuenta.views.cuenta, name="cuenta"),
    path('cuenta/registrar/', cuenta.views.registrar, name="cuenta_registrar"),
    path('cuenta/iniciar/', cuenta.views.iniciar_sesion, name="iniciar_sesion"),
    path('cuenta/cerrar/', cuenta.views.cerrar_sesion, name="cerrar_sesion"),
    path('cuenta/cambiarPassword/', cuenta.views.cambiarPassword, name="cambiarPassword"),
    #path('cuenta/cambiaEmail/', views.cambiarEmail),
    #path('cuenta/creada/', views.cuenta_creada),    
]
