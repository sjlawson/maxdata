from django.db import models
from django.db import IntegrityError
from django.db import transaction


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

    class Meta:
        db_table = 'genre_artist'
        unique_together = ['genre_id', 'artist_id']

    @staticmethod
    def import_from_csv_dataframe(df):
        objs = [GenreArtist(**vals) for vals in df.to_dict('records')]
        try:
            with transaction.atomic():
                GenreArtist.objects.bulk_create(objs)
        except IntegrityError:
            for obj in objs:
                try:
                    obj.save()
                except IntegrityError:
                    continue

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
