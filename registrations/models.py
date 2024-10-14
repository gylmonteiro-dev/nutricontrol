from django.db import models
from django.contrib.auth.models import User
from . import variables_choices


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="perfil", verbose_name="Usuário"
    )
    place = models.ForeignKey(
        "Place",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="perfis",
        verbose_name="Local de lotação",
    )
    phone_number = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Número de telefone"
    )
    registration_number = models.CharField(
        max_length=30, verbose_name="CPF ou CNPJ", default="SEM CADASTRO"
    )

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    unit_of_measurement = models.CharField(
        max_length=10,
        choices=variables_choices.UNIT_OF_MEASUREMENT,
        verbose_name="Unidade de medida",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")
    registration_number = models.CharField(
        max_length=30, verbose_name="CPF ou CNPJ", default="SEM CADASTRO"
    )

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")
    registration_number = models.CharField(
        max_length=30, verbose_name="CPF ou CNPJ", default="SEM CADASTRO"
    )

    def __str__(self):
        return self.name
