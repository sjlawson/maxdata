from django.db import models


class GenreArtist(models.Model):
    genre = models.ForeignKey(
        "Genre", related_name="genre_artists", on_delete=models.DO_NOTHING
    )
    artist = models.ForeignKey(
        "Artist", related_name="genre_artists", on_delete=models.DO_NOTHING
    )
    is_primary = models.BooleanField(default=True)
