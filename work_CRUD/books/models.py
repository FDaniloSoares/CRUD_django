from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.


class AuthorNameManager(models.Manager):
    
    def create_author(self, author_name):
        author, created = self.get_or_create(author_name=author_name)
        if created==True:
            return author
        else:
            print('This Author is already cadastraded')  
        
    def read_author(self, author_name):
        try:
            author = self.get(author_name__exact=author_name)
            return author
        except:
            print('Author {} not found.Please include the Author'.format(author_name))

    # Changing Authur Name
    def update_author(self, author_name, new_author_name):
        if self.all().filter(author_name=author_name).exists():
            self.update(author_name=new_author_name)
        else:
            print('Author {} not found.Please include the Author'.format(author_name))

    def delete_author(self, author_name):
        author = self.all().filter(author_name=author_name) 
        if author.exists():
            author.delete()
        else:
            print('Author {} not found'.format(author_name))
    


class AuthorName(models.Model):
    author_name = models.CharField('Nome', max_length=100 )
    
    def __str__(self):
        return self.author_name
    
    objects = AuthorNameManager()

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=100)
    edition = models.DecimalField('edition', max_digits=6, decimal_places=3)
    publication_year = models.DateField('publication_year')
    authors = models.ManyToManyField(AuthorName)

    def __str__(self):  
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']