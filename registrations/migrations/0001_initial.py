# Generated by Django 5.1.2 on 2024-10-11 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mame", models.CharField(max_length=200, verbose_name="Nome")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
                (
                    "registration_number",
                    models.CharField(
                        default="SEM CADASTRO",
                        max_length=30,
                        verbose_name="CPF ou CNPJ",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Nome")),
                (
                    "unit_of_measurement",
                    models.CharField(
                        choices=[
                            ("kg", "Kilograma"),
                            ("g", "Grama"),
                            ("un", "Unidade"),
                            ("litro", "Litro"),
                            ("ml", "Mililitro"),
                            ("cx", "Caixa"),
                            ("pc", "Pacote"),
                        ],
                        max_length=10,
                        verbose_name="Unidade de medida",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Suppliers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Nome")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
                (
                    "registration_number",
                    models.CharField(
                        default="SEM CADASTRO",
                        max_length=30,
                        verbose_name="CPF ou CNPJ",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "registration_number",
                    models.CharField(
                        default="SEM CADASTRO",
                        max_length=30,
                        verbose_name="CPF ou CNPJ",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Perfil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
