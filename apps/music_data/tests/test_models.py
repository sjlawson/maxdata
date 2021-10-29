import random
from django.test import TestCase
from common.test_helpers.faker import faker
from time import time

from apps.music_data.models.artist import Artist
from apps.music_data.models.genre import Genre
from apps.music_data.models.genre_artist import GenreArtist


def create_artist(**kwargs):
    defaults = {
        "name": f"{faker.first_name()} {faker.last_name()}",
        "export_date": int(time()),
        "is_actual_artist": True,
        "view_url": faker.uri(),
        "artist_type_id": random.randint(1, 20),
    }
    if kwargs:
        defaults.update(kwargs)
    return Artist.objects.create(**defaults)


def create_genre(**kwargs):
    defaults = {
        "name": faker.music_genre(),
        "parent": None,
        "export_date": int(time()),
    }
    if kwargs:
        defaults.update(kwargs)
    return Genre.objects.create(**defaults)


class ModelCreationTests(TestCase):
    def test_create_artist(self):
        artist = create_artist()
        self.assertTrue(isinstance(artist, Artist))
        self.assertEqual(artist.__unicode__(), artist.name)

    def test_create_genre(self):
        genre = create_genre()
        self.assertTrue(isinstance(genre, Genre))
        self.assertEqual(genre.__unicode__(), genre.name)

    def test_create_genre_artist(self):
        artist = create_artist()
        genre = create_genre()
        genre_artist = GenreArtist.objects.create(genre=genre, artist=artist)
        self.assertTrue(isinstance(genre_artist, GenreArtist))
        self.assertEqual(genre_artist.genre.name, genre.__unicode__())
        self.assertEqual(genre_artist.artist.name, artist.__unicode__())
