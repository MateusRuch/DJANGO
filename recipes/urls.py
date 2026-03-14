from django.urls import path
from recipes.views import home, contato, sobre
from django.contrib import admin

# HTTP request
# HTTP response
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    
    # Uma string vazia retornará para o link inicial do site, não sendo
    # necessário digitar /algo/ no ip.
]