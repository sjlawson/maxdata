from django.db import models


class GenreArtist(models.Model):
    export_date = models.PositiveBigIntegerField(null=True)
    genre_id = models.IntegerField(null=True)
    artist_id = models.IntegerField(null=True)
    is_primary = models.BooleanField(default=True)
    # artist = models.ForeignKey(
    #     "Artist",
    #     related_name="sub_genres",
    #     on_delete=models.DO_NOTHING,
    #     null=True,
    #     blank=True,
    #     db_constraint=False
    # )

    @staticmethod
    def import_from_csv_dataframe(df):
        df.rename(columns={'artist_id': 'id'}, inplace=True)
        GenreArtist.objects.bulk_create(
            GenreArtist(**vals) for vals in df.to_dict('records')
        )

    # @property
    # def artist(self):
    #     if self.artist_id:
    #         return Artist.objects.get(pk=self.artist_id)
    #     return None
    #
    # @property
    # def genre(self):
    #     if self.genre_id:
    #         return Genre.objects.get(pk=self.genre_id)
    #     return None
