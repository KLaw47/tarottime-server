# Generated by Django 4.1.3 on 2023-04-29 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("type", models.CharField(max_length=50)),
                ("name_short", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("meaning_up", models.CharField(max_length=100)),
                ("meaning_rev", models.CharField(max_length=100)),
                ("desc", models.CharField(max_length=500)),
                ("suit", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Reading",
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
                ("ques", models.CharField(max_length=50)),
                ("answer", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=50)),
                ("uid", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ReadingCard",
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
                    "card_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tarottimeapi.card",
                    ),
                ),
                (
                    "reading_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tarottimeapi.reading",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="reading",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tarottimeapi.user"
            ),
        ),
    ]
