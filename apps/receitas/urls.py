from django import views
from django.urls import path

from .views import * # faz o importa das minhas views dentro do init

urlpatterns = [
    path("", index, name="index" ),
    path("<int:receita_id>", receitaViews, name="receita" ),
    path('buscar/', busca, name='buscar'),
    path("criar/receita/", criar_receita, name="criar_receita" ),
    path("deletar/receita/<int:receita_id>", deleta_receita, name="deleta_receita" ),
    path("editar/receita/<int:receita_id>", edita_receita, name="edita_receita" ),
    path("atualiza/receita/", atualiza_receita, name="atualiza_receita" ),
]   