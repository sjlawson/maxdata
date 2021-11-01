from django.db import models
from django.db import IntegrityError
from django.db import transaction


class GenreArtist(models.Model):
    export_date = models.PositiveBigIntegerField(null=True)
    genre_id = models.IntegerField(null=True)
    artist_id = models.IntegerField(null=True)
    is_primary = models.BooleanField(default=True)

    class Meta:
        db_table = "genre_artist"
        unique_together = ["genre_id", "artist_id"]

    @staticmethod
    def import_from_csv_dataframe(df):
        objs = [GenreArtist(**vals) for vals in df.to_dict("records")]
        try:
            # if there's an integrity error on a bulk_create,
            # the atomic block does not close
            with transaction.atomic():
                GenreArtist.objects.bulk_create(objs)
        except IntegrityError:
            for obj in objs:
                try:
                    # expecting integrity error, so also need atomic
                    with transaction.atomic():
                        obj.save()
                except IntegrityError:
                    continue
