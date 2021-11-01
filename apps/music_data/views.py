from django.shortcuts import render
from django.http import HttpResponse
from pandas import DataFrame
from apps.music_data.models import query_helpers


def index(request):
    return render(request, "index.html")


def genres_by_artist(request, artist_id):
    data = query_helpers.get_genres_by_artist(artist_id)
    df = DataFrame(data)
    return HttpResponse(df.to_html())


def artists_by_genre(request, genre_id):
    data = query_helpers.get_artists_by_genre(genre_id)
    df = DataFrame(data)
    return HttpResponse(df.to_html())


def artists_by_genre_count(request, limit=100, offset=0):
    data = query_helpers.get_artists_ordered_by_genre_count(limit, offset)
    df = DataFrame(data)
    return HttpResponse(df.to_html())


def genres_by_artist_count(request, limit=100, offset=0):
    data = query_helpers.get_genres_ordered_by_artist_count()
    df = DataFrame(data)
    return HttpResponse(df.to_html())


def orphan_genres(request):
    data = query_helpers.get_orphan_genres()
    df = DataFrame(data)
    return HttpResponse(df.to_html())


def orphan_artists(request):
    data = query_helpers.get_orphan_artists()
    df = DataFrame(data)
    return HttpResponse(df.to_html())
