from django.db import connection

"""
Django is great for a lot of things, but not for joining tables without a foreign key.
At first it looks like these table should be related, but on import, if the foreign key field
doesn't link up with the related table because of import order, the data gets dropped.
It seems, in this case, preservation of data is the important thing, and then the relationships
can be expressed with SQL queries.
Had this been a stand-alone app with no possibility of scaling further or adding
new features or apps, Flask might also be a good choice as framework for this, since
SQLAlchemy is a little bit more flexible regarding JOIN queries lacking foreign keys.
"""
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]


def get_genres_by_artist(artist_id):
    sql = """
    SELECT g.* FROM genres AS g
    INNER JOIN genre_artist ga ON ga.genre_id = g.id
    INNER JOIN artists AS a ON a.id = ga.artist_id
    WHERE a.id = %s"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [artist_id])
        return dictfetchall(cursor)


def get_artists_by_genre(genre_id):
    sql = """
    SELECT a.* FROM artists AS a
    INNER JOIN genre_artist AS ga ON ga.artist_id = a.id
    INNER JOIN genres AS g ON ga.genre_id = g.id
    WHERE g.id = %s"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [genre_id])
        return dictfetchall(cursor)


def get_artists_ordered_by_genre_count(limit=None, offset=None):
    sql = """
    SELECT a.*, count(g.id) AS genre_count
    FROM artists a INNER JOIN genre_artist ga ON a.id = ga.artist_id
    INNER JOIN genres g ON ga.genre_id = g.id
    GROUP BY a.id ORDER BY genre_count DESC
    """
    if limit:
        sql += ' LIMIT %s'
    if offset:
        sql += f' OFFSET %s'
    params = [_ for _ in [limit, offset] if _]
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        return dictfetchall(cursor)


def get_genres_ordered_by_artist_count():
    sql = """
    SELECT g.*, count(a.id) AS artist_count FROM genres g
    LEFT JOIN genre_artist ga ON g.id = ga.genre_id
    INNER JOIN artists a ON a.id = ga.artist_id
    GROUP BY g.id ORDER BY artist_count DESC
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)


def get_orphan_genres():
    sql = """
    SELECT g.* FROM genres g
    LEFT JOIN genre_artist ga ON g.id = ga.genre_id
    WHERE ga.id IS NULL
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)


def get_orphan_artists():
    sql = """
    SELECT a.* FROM artists a
    LEFT JOIN genre_artist ga ON a.id = ga.artist_id
    WHERE ga.id IS NULL
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)
