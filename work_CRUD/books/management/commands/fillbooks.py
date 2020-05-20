from django.core.management.base import BaseCommand, CommandError
from work_CRUD.books.models import Book, Books
from work_CRUD.books.models import BookManager

import json

class Command(BaseCommand):
    help = 'Populating books'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")
    
    def handle(self, *args, **options):

        file_path = options['path']
        with open(file_path, 'r') as json_file:
            jsonreader = json.load(json_file)
            
            print(jsonreader)
            
            books = Books(
                name = jsonreader['name'],
                edition = jsonreader['edition'],
                publication_year = jsonreader['publication_year']   
            )
            books.save()

            for author in jsonreader['authors']:
                print(author)
                book = Book.objects.create_book(author) 
                books.authors.add(book)
