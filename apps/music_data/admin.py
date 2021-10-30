from django.contrib import admin
from . import models


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(models.GenreArtist)
class GenreArtistAdmin(admin.ModelAdmin):
    list_display = ("genre_id", "artist_id", "is_primary")
    search_fields = ("genre_id", "artist_id", "is_primary")
