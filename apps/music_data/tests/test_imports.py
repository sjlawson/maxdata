import os
from django.test import TestCase
from apps.music_data.helpers import read_max_csv, get_model_by_pk
from apps.music_data.models import Genre, Artist, GenreArtist

class ImportTests(TestCase):

    def test_import_genre(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/genretest')
        self.assertEqual(pk, 'genre_id')
        print(df)  # shows that there are 7 records in the dataframe, but one is duplicate
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)
        records = Genre.objects.count()
        self.assertEqual(records, 6)

    def test_import_artist(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/artisttest')
        self.assertEqual(pk, 'artist_id')
        print(df)
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)
        records = Artist.objects.count()
        self.assertEqual(records, 5)


    def test_import_artist(self):
        pk, df = read_max_csv(f'{os.path.dirname(__file__)}/genre_artisttest')
        self.assertEqual(pk, 'genre_id\x01artist_id')
        print(df)
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)
        records = GenreArtist.objects.count()
        self.assertEqual(records, 4)
