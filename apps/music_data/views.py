from django.shortcuts import render
from django.http import HttpResponse
from pandas import DataFrame
from apps.music_data.models import query_helpers, Artist, Genre


def index(request):
    return render(request, "index.html")


def genres_by_artist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    data = query_helpers.get_genres_by_artist(artist_id)
    df = DataFrame(data)
    return render(
        request,
        "genres_by_artist.html",
        {"df_html": df.to_html(index=False), "artist_name": artist.name},
    )


def artists_by_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    data = query_helpers.get_artists_by_genre(genre_id)
    df = DataFrame(data)
    return render(
        request,
        "artists_by_genre.html",
        {"df_html": df.to_html(index=False), "genre_name": genre.name},
    )


def artists_by_genre_count(request, limit=100, offset=0):
    data = query_helpers.get_artists_ordered_by_genre_count(limit, offset)
    df = DataFrame(data)
    return render(
        request, "artists_by_genre_count.html", {"df_html": df.to_html(index=False)}
    )


def genres_by_artist_count(request, limit=100, offset=0):
    data = query_helpers.get_genres_ordered_by_artist_count()
    df = DataFrame(data)
    return render(
        request, "genres_by_artist_count.html", {"df_html": df.to_html(index=False)}
    )


def orphan_genres(request):
    data = query_helpers.get_orphan_genres()
    df = DataFrame(data)
    return render(request, "orphan_genres.html", {"df_html": df.to_html(index=False)})


def orphan_artists(request, limit=100, offset=0):
    data = query_helpers.get_orphan_artists(limit, offset)
    df = DataFrame(data)
    return render(request, "orphan_artists.html", {"df_html": df.to_html(index=False)})
