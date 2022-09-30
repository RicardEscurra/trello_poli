# Generated by Django 4.1.1 on 2022-09-30 18:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Backlog",
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
                ("posicion", models.IntegerField(null=True)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("Product_Backlog", "Product_Backlog"),
                            ("Sprint_Backlog", "Sprint_Backlog"),
                            ("Doing", "Doing"),
                            ("To_Do", "To_Do"),
                            ("Done", "Done"),
                        ],
                        max_length=16,
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        choices=[("Vacio", "Vacio"), ("Cargado", "Cargado")],
                        default="Vacio",
                        max_length=8,
                    ),
                ),
                ("fechaCreacion", models.DateField(auto_now_add=True)),
                ("numTareas", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Historial",
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
                ("categoria", models.CharField(max_length=80)),
                ("operacion", models.CharField(max_length=150)),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                ("autor", models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Miembro",
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
            ],
        ),
        migrations.CreateModel(
            name="Proyecto",
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
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.TextField(max_length=200)),
                ("fechaCreacion", models.DateField(auto_now_add=True)),
                ("fechaInicio", models.DateField(null=True)),
                ("fechaFin", models.DateField(null=True)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Pendiente", "Pendiente"),
                            ("Iniciado", "Iniciado"),
                            ("Cancelado", "Cancelado"),
                            ("Finalizado", "Finalizado"),
                        ],
                        default="Pendiente",
                        max_length=10,
                    ),
                ),
                ("numSprints", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Rol",
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
                ("nombre", models.CharField(max_length=50)),
            ],
            options={
                "permissions": (
                    ("Crear proyecto", "Permite crear proyectos"),
                    ("Modificar proyecto", "Permite modificar proyectos"),
                    ("Eliminar proyecto", "Permite eliminar proyectos"),
                    ("Crear Sprint", "Permite crear un sprint"),
                    ("Modificar Sprint", "Permite modificar un sprint"),
                    ("Cancelar Sprint", "Permite cancelar un sprint"),
                    ("Crear user story", "Permite crear un user story"),
                    ("Modificar user story", "Permite modificar un user story"),
                    ("Eliminar user story", "Permite eliminar un user story"),
                ),
            },
        ),
        migrations.CreateModel(
            name="Sprint",
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
                ("objetivos", models.CharField(max_length=300, null=True)),
                ("posicion", models.IntegerField(null=True)),
                ("numTareas", models.IntegerField(default=0)),
                ("duracion", models.IntegerField(default=0)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("En_cola", "En cola"),
                            ("Activo", "Activo"),
                            ("Cancelado", "Cancelado"),
                            ("Finalizado", "Finalizado"),
                        ],
                        default="En_cola",
                        max_length=10,
                    ),
                ),
                ("fechaCreacion", models.DateField(auto_now_add=True)),
                ("fechaInicio", models.DateField(null=True)),
                ("fechaFin", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserStory",
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
                ("nombre", models.CharField(max_length=150)),
                ("descripcion", models.TextField(max_length=300)),
                ("estado", models.CharField(default="En_Cola", max_length=7)),
                ("fechaCreacion", models.DateField(auto_now_add=True)),
                ("fechaInicio", models.DateField(null=True)),
                ("fechaFin", models.DateField(null=True)),
                ("identificador", models.CharField(max_length=80, null=True)),
                (
                    "prioridad",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "backlog",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_stories",
                        to="proyectos.backlog",
                    ),
                ),
            ],
        ),
    ]
