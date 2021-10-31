import os
from django.test import TestCase
from apps.music_data.helpers import read_max_csv, get_model_by_pk
from apps.music_data.models.query_helpers import *

class MAXQueryTests(TestCase):

    def setUp(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/genretest')
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)

        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/artisttest')
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)

        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/genre_artisttest')
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)


    def test_get_genres_by_artist(self):
        genres = get_genres_by_artist(10767)
        self.assertEqual(genres[0]['name'], 'Blues')

    def test_get_artists_by_genre(self):
        artists = get_artists_by_genre(2)
        self.assertEqual(artists[0]['name'],'Charles Foxx')

    def test_get_artists_ordered_by_genre_count(self):
        artists = get_artists_ordered_by_genre_count()
        from jpprint import jpprint
        jpprint(artists)

    def test_get_genres_ordered_by_artist_count(self):
        res = get_genres_ordered_by_artist_count()
        from jpprint import jpprint
        jpprint(res)

    def test_get_orphan_artists(self):
        artists = get_orphan_artists()
        from jpprint import jpprint
        jpprint(artists)

    def test_get_orphan_genres(self):
        genres = get_orphan_genres()
        from jpprint import jpprint
        jpprint(artists)
