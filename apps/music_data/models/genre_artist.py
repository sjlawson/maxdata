from django.db import models


class GenreArtist(models.Model):
    export_date = models.PositiveBigIntegerField(null=True)
    genre_id = models.IntegerField(null=True)
    artist_id = models.IntegerField(null=True)
    is_primary = models.BooleanField(default=True)


    @staticmethod
    def import_from_csv_dataframe(df):
        df.rename(columns={'artist_id': 'id'}, inplace=True)
        GenreArtist.objects.bulk_create(
            GenreArtist(**vals) for vals in df.to_dict('records')
        )
