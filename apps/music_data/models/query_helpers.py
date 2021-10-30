from django.db import connection
from . import Artist, Genre, GenreArtist


def get_artist_genres(artist_id):
    sql = """
    """
    pass

def get_gernre_artists(genre_id):
    sql = """
    """
    pass

def get_multi_genre_artists():
    sql = """SELECT a.*, count(g.id) AS genre_count
        FROM artists a INNER JOIN genre_artist ga ON a.id = ga.artist_id
        INNER JOIN genres g ON ga.genre_id = g.id
        GROUP BY g.id ORDER BY genre_count DESC
    """
    pass

def get_genres_by_artist_count():
    sql = """
    """
    pass

def get_gernres_by_multi_genre_artists():
    sql = """
    """
    pass

def get_orphan_genrea():
    sql = """
    """
    pass

def get_orphan_artists():
    sql = """
    """
    pass
