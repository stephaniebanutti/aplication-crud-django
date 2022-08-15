from email import message
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User   #importa o modelo de usuarios
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if verifica_campo(nome):
            messages.error(request, "O campo nome não pode ser vazio.")
            return redirect('cadastro')
        if verifica_campo(email):
            messages.error(request, "O campo email não pode ser vazio.")
            return redirect('cadastro')
        if validacao_senha(senha, senha2):
            messages.error(request, "As senhas não coincidem")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists(): #verifica se existe na minha tabela de users
            messages.error(request, "Usuario já cadastrado.")
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists(): #verifica se existe na minha tabela de users
            messages.error(request, "Usuário existente.")
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, "Cadastro criado com sucesso." )
        return redirect('login') #redireciona para outra pagina, ele vai pelo name da url
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        if verifica_campo(email) and verifica_campo(senha):
            messages.error(request, "Os campos email e senha não ser ficar vazios.")
            return redirect('login')
        print(email, senha)
    
        if User.objects.filter(email=email).exists(): #se o objeto email existir
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() #pega meu username em base do meu email digitado
            user = auth.authenticate(request, username=nome, password=senha) # faz a autenticação do username e senha para logar
            if user is not None: # se o usuario não for vazio
                auth.login(request, user) # libera para prosseguir e entrar
                messages.success(request, "Login realizado com sucesso")
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=request.user.id)

        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
       return redirect('index') 

def logout(request):
    auth.logout(request)
    return redirect('index')

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
        return render(request, 'usuarios/criar_receita.html')


def verifica_campo(campo):
    return not campo.strip()

def validacao_senha(senha, senha2):
    return senha != senha2