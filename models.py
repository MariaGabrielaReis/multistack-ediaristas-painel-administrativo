from django.db import models


class Housekeeper(models.Model):
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    logradouro = models.CharField(max_length=60, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    complemento = models.CharField(max_length=100, null=False, blank=False)
    codigo_ibge = models.IntegerField(null=False, blank=False)
    foto = models.ImageField(null=False)
