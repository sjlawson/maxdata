# Generated by Django 3.2.8 on 2021-10-30 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_data', '0006_alter_genre_parent_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='artist',
            table='artists',
        ),
        migrations.AlterModelTable(
            name='genre',
            table='genres',
        ),
        migrations.AlterModelTable(
            name='genreartist',
            table='genre_artist',
        ),
    ]