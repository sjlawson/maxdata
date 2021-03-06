# Generated by Django 3.2.8 on 2021-11-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
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
                ("name", models.CharField(max_length=1000)),
                ("export_date", models.PositiveBigIntegerField()),
                ("is_actual_artist", models.BooleanField(default=True)),
                ("view_url", models.CharField(max_length=1000)),
                ("artist_type_id", models.IntegerField()),
            ],
            options={
                "db_table": "artists",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("parent_id", models.IntegerField(default=None, null=True)),
                ("name", models.CharField(max_length=200)),
                ("export_date", models.PositiveBigIntegerField()),
            ],
            options={
                "db_table": "genres",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="GenreArtist",
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
                ("export_date", models.PositiveBigIntegerField(null=True)),
                ("genre_id", models.IntegerField(null=True)),
                ("artist_id", models.IntegerField(null=True)),
                ("is_primary", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "genre_artist",
                "unique_together": {("genre_id", "artist_id")},
            },
        ),
    ]
