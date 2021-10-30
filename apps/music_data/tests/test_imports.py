import os
from django.test import TestCase
from apps.music_data.helpers import read_max_csv, get_model_by_pk

class ImportTests(TestCase):

    def test_import_genre(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/genretest')
        self.assertEqual(pk, 'genre_id')
        print(df)

        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)

    def test_import_artist(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/artisttest')
        self.assertEqual(pk, 'artist_id')
        print(df)

        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)


    def test_import_artist(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/genre_artisttest')
        self.assertEqual(pk, 'genre_id\x01artist_id')
        print(df)

        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)
