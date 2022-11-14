from django.db import models

# Create your models here.
# Model para definição da tabela usuários no banco

class Users(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthDate = models.DateField()

