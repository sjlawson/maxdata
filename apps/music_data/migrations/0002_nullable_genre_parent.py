# Generated by Django 3.2.8 on 2021-10-29 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("music_data", "0001_music_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_genres",
                to="music_data.genre",
            ),
        ),
    ]