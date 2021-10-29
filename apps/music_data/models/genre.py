from django.db import models


class Genre(models.Model):
    parent = models.ForeignKey(
        "Genre",
        related_name="sub_genres",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=200)
    export_date = models.PositiveBigIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
