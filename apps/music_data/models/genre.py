from django.db import models
from pandas import DataFrame


class Genre(models.Model):
    # parent = models.ForeignKey(
    #     "Genre",
    #     related_name="sub_genres",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    #     db_constraint=False
    # )
    parent_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    export_date = models.PositiveBigIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    @staticmethod
    def import_from_csv_dataframe(df:DataFrame):
        df.rename(columns={'genre_id': 'id'}, inplace=True)
        Genre.objects.bulk_create(
            Genre(**vals) for vals in df.to_dict('records')
        )
