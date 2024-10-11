from django.db import models
from django.contrib.auth.models import User
from choices import UNIT_OF_MEASUREMENT


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='Perfil')
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    unit_of_measurement = models.CharField(max_length=10, choices=UNIT_OF_MEASUREMENT, verbose_name='Unidade de medida')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')
    who_registred = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=True)
    


class Suppliers(models.Model):
    ...


class Place(models.Model):
    ...

