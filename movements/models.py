from django.db import models
from django.core.validators import MinValueValidator
from registrations.models import Place, Supplier, Product

# Create your models here.


class ProductEntry(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="list_products",
        verbose_name="Listagem de Produto",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    amount = models.IntegerField(
        validators=[MinValueValidator(1, 'Não pode ser menor que 1')], verbose_name="Quantidade"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")

    def __str__(self) -> str:
        return f"{self.product} | {self.amount}.{self.product.unit_of_measurement}"


class StockEntry(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.PROTECT, related_name="entries", verbose_name="Local"
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="entries",
        verbose_name="Fornecedor",
    )
    list_products = models.ManyToManyField(
        ProductEntry, related_name="entries", verbose_name="Lista de Produtos"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")

    def __str__(self) -> str:
        return f"{self.id}"
