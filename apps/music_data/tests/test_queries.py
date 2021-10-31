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
        result_set = [{'name': _['name']} for _ in artists]
        expected = [{'name': 'Charles Foxx'}, {'name': 'Charles Luke'}]
        self.assertCountEqual(result_set, expected)

    def test_get_artists_ordered_by_genre_count(self):
        artists = get_artists_ordered_by_genre_count()
        self.assertEqual(artists[0]['genre_count'], 2)

    def test_get_genres_ordered_by_artist_count(self):
        res = get_genres_ordered_by_artist_count()
        expected = [
            {
                "artist_count": 2,
                "export_date": 1625549384231,
                "id": 2,
                "name": "Blues",
                "parent_id": 34
            },
            {
                "artist_count": 1,
                "export_date": 1625549384231,
                "id": 37,
                "name": "Tones",
                "parent_id": 0
            }
        ]
        self.assertCountEqual(res, expected)

    def test_get_orphan_artists(self):
        artists = get_orphan_artists()
        expected = [
            {
                "artist_type_id": 1,
                "export_date": 1625549384231,
                "id": 313091,
                "is_actual_artist": True,
                "name": "Walter Melrose",
                "view_url": "https://itunes.apple.com/artist/walter-melrose/id313091?uo=5"
            },
            {
                "artist_type_id": 1,
                "export_date": 1625549384231,
                "id": 313592,
                "is_actual_artist": True,
                "name": "Susanne Norin",
                "view_url": "https://itunes.apple.com/artist/susanne-norin/id313592?uo=5"
            }
        ]
        self.assertCountEqual(artists, expected)


    def test_get_orphan_genres(self):
        genres = get_orphan_genres()
        expected = [
            {
                "export_date": 1625549384231,
                "id": 27,
                "name": "J-Pop",
                "parent_id": 34
            },
            {
                "export_date": 1625549384231,
                "id": 28,
                "name": "Enka",
                "parent_id": 34
            },
            {
                "export_date": 1625549384231,
                "id": 29,
                "name": "Anime",
                "parent_id": 34
            },
            {
                "export_date": 1625549384231,
                "id": 38,
                "name": "eBooks",
                "parent_id": 0
            }
        ]
        self.assertCountEqual(genres, expected)
