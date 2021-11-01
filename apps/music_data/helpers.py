import pandas as pd
from io import StringIO
from apps.music_data.models import Artist, Genre, GenreArtist


models_pk = {
    "artist_id": Artist,
    "genre_id": Genre,
    "genre_id\x01artist_id": GenreArtist,
}


def read_max_csv(filename):
    """
    param: filename
    return string, DataFrame
    """
    with open(filename) as f:
        headers = str(f.readline())[1:].rstrip("\x02\n").split(chr(1))
        pk = str(f.readline())
        pk = pk[pk.find(":") + 1 : -2]
        row_count = 1
        for row in f:
            row_count += 1
            if row[0] != "#":
                f.seek(0)
                break

        df = pd.read_csv(f, skiprows=row_count, sep=chr(1), names=headers)
        df.iloc[:, -1:] = df.iloc[:, -1:].apply(lambda s: s.str.rstrip(chr(2)))
        df.fillna(0, inplace=True)
        return pk, df[~df["export_date"].astype(str).str.contains("#")]


def get_model_by_pk(pk):
    return models_pk[pk]
