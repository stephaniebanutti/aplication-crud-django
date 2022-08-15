from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Receita
from django.contrib import auth, messages
from django.contrib.auth.models import User #importa o modelo de usuarios
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #Modulos para importar a paginação

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada='True')
    paginator = Paginator(receitas, 3) # var pegando meus parametros de quais dados vou colocar em paginação, e a quantidade de dados que vai aparecer na tela
    page = request.GET.get('page') #indentificar a pagina que está na navegação entre as paginas
    receitas_por_pagina = paginator.get_page(page) #definição quantas receitas aparecem por paginas
    
    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request, "receitas/index.html", dados)


def receitaViews(request, receita_id): #traz como parametro o id das receitas 
    receita = get_object_or_404(Receita, pk=receita_id)
    # Nessa linha eu pego o valor do meu objeto e informo que ele é uma primare key
    receita_atual = {
        'receita': receita
    }
    return render(request, "receitas/receita.html", receita_atual)


def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        usuario = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=usuario,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/criar_receita.html')

def deleta_receita(request, receita_id): #pega o parametro do id
    receita = get_object_or_404(Receita, pk=receita_id) # localiza o objeto id da class Receita e o id pelo pk e retorna numa var
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id): #pega o parametro do id
    receita = get_object_or_404(Receita, pk=receita_id) # localiza o objeto id da class Receita e o id pelo pk e retorna numa var
    receita_a_editar = { 'receita': receita}
    return render(request, 'receitas/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    if request.method == "POST":
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id) #aqui diz qual receita que quero editar
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES: #se tiver alguma coisa dentro do campo da foto
            r.foto_receita = request.FILES['foto_receita']
        r.save()

        return redirect('dashboard')
