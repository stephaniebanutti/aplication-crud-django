from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index" ),
    path("<int:receita_id>", views.receitaViews, name="receita" ),
    path('buscar/', views.buscar, name='buscar')
]