from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True, null=True)