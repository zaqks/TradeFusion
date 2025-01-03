# Generated by Django 4.2.11 on 2024-11-01 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wilaya",
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
                ("code", models.IntegerField()),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=13, null=True)),
                ("password", models.CharField(max_length=64, null=True)),
                ("last_logged", models.DateTimeField(auto_now=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("C", "Customer"), ("O", "Owner"), ("G", "Guest")],
                        default="C",
                        max_length=20,
                    ),
                ),
                ("name", models.CharField(max_length=64, null=True)),
                ("surname", models.CharField(max_length=64, null=True)),
                (
                    "wil",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_app.wilaya",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerSession",
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
                ("token", models.CharField(max_length=32)),
                ("created", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_app.customuser",
                    ),
                ),
            ],
        ),
    ]
