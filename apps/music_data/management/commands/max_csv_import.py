from django.core.management.base import BaseCommand
from apps.music_data.helpers import read_max_csv, get_model_by_pk

class Command(BaseCommand):
    help = 'Import MAX formatted csv file: manage.py max_csv_import <filename>'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='name of file to import')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        pk, df = read_max_csv(filename)
        model = get_model_by_pk(pk)
        model.import_from_csv_dataframe(df)
