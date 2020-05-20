from django.core.management.base import BaseCommand, CommandError
from work_CRUD.books.models import Book
from work_CRUD.books.models import BookManager

import pandas as pd 

class Command(BaseCommand):
    help = 'Creating model objects/ populatin actor name'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")
    
    def handle(self, *args, **options):
        #_model = Book()
        file_path = options['path']
        with open(file_path, 'rb'):
            reader = pd.read_csv(file_path)
            
            lis = reader.values.tolist()
            
            counter = 0 
            for k in lis:                 
                Book.objects.create_book(lis[counter][0])
                counter = counter + 1