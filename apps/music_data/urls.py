from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="max_index"),
    path(
        "genres_by_artist/<int:artist_id>",
        views.genres_by_artist,
        name="genres_by_artist",
    ),
    path(
        "artists_by_genre/<int:genre_id>",
        views.artists_by_genre,
        name="artists_by_genre",
    ),
    path(
        "artists-by-genre-count/",
        views.artists_by_genre_count,
        name="artists_ordered_by_genre_count",
    ),
    path(
        "genres_by_artist_count/",
        views.genres_by_artist_count,
        name="genres_ordered_by_artist_count",
    ),
    path("orphan_genres/", views.orphan_genres, name="orphan_genres"),
    path("orphan_artists/", views.orphan_artists, name="orphan_artists"),
]
