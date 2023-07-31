"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from core.views import index,detalhe_filme
from categoria.views import categoria_criar,categoria_editar,categoria_listar,categoria_remover
from filme.views import filme_listar,filme_criar,filme_editar,filme_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('detalhe_filme/<int:id>/',detalhe_filme,name='detalhe_filme'),

    path('categoria/',categoria_criar,name='categoria_criar'),
    path('categoria/editar/<int:id>/',categoria_editar,name='categoria_editar'),
    path('categoria/remover/<int:id>/',categoria_remover,name='categoria_remover'),
    path('categoria_listar',categoria_listar,name='categoria_listar'),

    path('filme/',filme_criar,name='filme_criar'),
    path('filme/editar/<int:id>/',filme_editar,name='filme_editar'),
    path('filme/remover/<int:id>/',filme_remover,name='filme_remover'),
    path('filme_listar',filme_listar,name='filme_listar'),
]
