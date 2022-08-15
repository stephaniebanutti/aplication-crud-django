
from receitas.models import Receita
from django.shortcuts import render, redirect


def busca(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada='True')
    
    if 'buscar' in request.GET: # verifica se o campo de busca do front possui algum valor
        nome_a_buscar = request.GET['buscar'] # Cria uma var e pega esse valor da url que foi enviada metodo get
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar) # da um novo valor para lista_receitas se tiver algum valor a exibir, __icontains significa que vai encontrar todos os resultados que tem essa palavra a buscar

    dados= {'receitas' : lista_receitas} # traz o resultado e manda pro front
    
    return render(request, "receitas/buscar.html", dados)