from django.db import models
from django.db import IntegrityError
from django.db import transaction


class Genre(models.Model):
    parent_id = models.IntegerField(null=True, default=None)
    name = models.CharField(max_length=200)
    export_date = models.PositiveBigIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "genres"
        ordering = ["name"]

    @staticmethod
    def import_from_csv_dataframe(df):
        df.rename(columns={"genre_id": "id"}, inplace=True)
        objs = [Genre(**vals) for vals in df.to_dict("records")]
        # this transaction.atomic try/exept code would be best moved to a helper or model mixin
        try:
            with transaction.atomic():
                Genre.objects.bulk_create(objs)
        except IntegrityError:
            for obj in objs:
                try:
                    with transaction.atomic():
                        obj.save()
                except IntegrityError:
                    obj.delete()
                    continue

    @property
    def parent(self):
        if self.parent_id:
            return Genre.objects.filter(id=self.parent_id).first()
        return None

    @property
    def artists(self):
        pass
