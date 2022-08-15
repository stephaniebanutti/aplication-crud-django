from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada') # Nomeia meus objetos lá do admin 
    list_display_links = ('id', 'nome_receita') #transforma meus campos em links
    search_fields = ('nome_receita',) # faz a busca dos meus dados (lista)
    list_filter = ('categoria',) #faz filtro das categorias
    list_per_page = 5 #limita a quantidade de dados na tela, colocando uma paginação
    list_editable = ('publicada',)

admin.site.register(Receita, ListandoReceitas) # Cria um grupo de receitas lá no meu admin
# é passado o argumento para organizar ao criar a instancia