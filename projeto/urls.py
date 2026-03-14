"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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


# HTTP request
# HTTP response
urlpatterns = [
    path('admin/', admin.site.urls),  # O path é uma função que recebe dois
    # argumentos: o primeiro é a string que representa a URL
    # e o segundo é a função que será chamada quando essa URL for acessada.
    path('', include("recipes.urls")),  # o include é uma função que permite
    # incluir URLs de outro módulo..
    # No caso de uma string vazia, o include irá procurar as URLs do módulo
    # recipes.urls e irá redirecionar para elas.

]
