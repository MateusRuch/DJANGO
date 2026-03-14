from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "recipes/home.html", context={
        "name": "Mateus",
    })  # a função render é usada
# para renderizar um template HTML e retornar uma resposta HTTP. O primeiro
# argumento é o objeto de solicitação, o segundo argumento é o caminho para o
# template HTML que queremos renderizar. O Django irá procurar por esse
# template na pasta "templates" dentro do diretório do aplicativo "recipes".
# Se o template for encontrado, ele será renderizado e retornado como resposta
# HTTP.


def sobre(request):
    return HttpResponse("Sobre")


def contato(request):
    return HttpResponse("Contato")
