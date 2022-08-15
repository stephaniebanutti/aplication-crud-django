from django.db import models

class Pessoa(models.Model):
    nome=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    
    def __str__(self): # retorna o nome do objeto referenciado
        return self.nome


#comando: python manage.py makemigrations
#Faz a migração dessa aplicação


#comando: python manage.py migrate
# manda essa migração criada para o banco