from django.db import models
from pandas import DataFrame


class Artist(models.Model):
    name = models.CharField(max_length=1000)
    export_date = models.PositiveBigIntegerField()
    is_actual_artist = models.BooleanField(default=True)
    view_url = models.CharField(max_length=1000)
    artist_type_id = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    @staticmethod
    def import_from_csv_dataframe(df:DataFrame):
        df.rename(columns={'artist_id': 'id'}, inplace=True)
        Artist.objects.bulk_create(
            Artist(**vals) for vals in df.to_dict('records')
        )
