from django.db import models
from django.db import IntegrityError
from django.db import transaction


class Artist(models.Model):
    name = models.CharField(max_length=1000)
    export_date = models.PositiveBigIntegerField()
    is_actual_artist = models.BooleanField(default=True)
    view_url = models.CharField(max_length=1000)
    artist_type_id = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'artists'
        ordering = ['name']

    @staticmethod
    def import_from_csv_dataframe(df):
        df.rename(columns={'artist_id': 'id'}, inplace=True)
        objs = [Artist(**vals) for vals in df.to_dict('records')]
        try:
            # best case - no dups, bul create
            with transaction.atomic():
                Artist.objects.bulk_create(objs)
        except IntegrityError:
            # must have been a dup, so try serial insertion
            for obj in objs:
                try:
                    obj.save()
                except IntegrityError:
                    continue
