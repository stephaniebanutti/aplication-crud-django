from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada='True')

    dados = {
        'receitas': receitas
    }
    
    return render(request, "index.html", dados)


def receitaViews(request, receita_id): #traz como parametro o id das receitas 
    receita = get_object_or_404(Receita, pk=receita_id)
    # Nessa linha eu pego o valor do meu objeto e informo que ele é uma primare key
    receita_atual = {
        'receita': receita
    }
    return render(request, "receita.html", receita_atual)


def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada='True')
    
    if 'buscar' in request.GET: # verifica se o campo de busca do front possui algum valor
        nome_a_buscar = request.GET['buscar'] # Cria uma var e pega esse valor da url que foi enviada metodo get
        
        if buscar: # condiciona, se tiver valor 
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar) # da um novo valor para lista_receitas se tiver algum valor a exibir, __icontains significa que vai encontrar todos os resultados que tem essa palavra a buscar

    dados= {'receitas' : lista_receitas} # traz o resultado e manda pro front
    
    return render(request, "buscar.html", dados)