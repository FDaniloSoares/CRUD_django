from django.core.management.base import BaseCommand, CommandError
from work_CRUD.books.models import Book
from work_CRUD.books.models import BookManager

import csv

class Command(BaseCommand):
    help = 'Creating model objects/ populatin actor name'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")
    
    def handle(self, *args, **options):
        #_model = Book()
        file_path = options['path']
        with open(file_path, 'r') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for author_name in csvreader:
                print(author_name)
                Book.objects.create_book(**author_name)