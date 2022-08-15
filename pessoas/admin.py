from django.contrib import admin
from .models import Pessoa


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email') # Nomeia meus objetos lá do admin 
    list_display_links = ('id', 'nome') #transforma meus campos em links
    search_fields = ('nome',) # faz a busca dos meus dados (lista)
    list_per_page = 5 #limita a quantidade de dados na tela, colocando uma paginação

admin.site.register(Pessoa, ListandoPessoas)