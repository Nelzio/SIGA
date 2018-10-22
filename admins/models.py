from django.db import models
from home.models import Endereco, Contacto


class Funcionario(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20)

