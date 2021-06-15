from django.db import models


class Housekeeper(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=12, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)
    address_number = models.IntegerField(null=False, blank=False)
    address_district = models.CharField(max_length=30, null=False, blank=False)
    address_complement = models.CharField(max_length=100, null=False, blank=False)
    address_cep = models.CharField(max_length=8, null=False, blank=False)
    address_state = models.CharField(max_length=2, null=False, blank=False)
    ibge_code = models.IntegerField(null=False, blank=False)
    user_photo = models.ImageField(null=False)
