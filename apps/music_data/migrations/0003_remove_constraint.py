# Generated by Django 3.2.8 on 2021-10-29 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("music_data", "0002_nullable_genre_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_genres",
                to="music_data.genre",
            ),
        ),
    ]
