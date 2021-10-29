from django.db import models


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
