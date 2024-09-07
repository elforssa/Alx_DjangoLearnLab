from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Author model represents an author with a name field.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model represents a book, including title, publication year, and
    a foreign key relationship to the Author model.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    """
    Represents an author who can write multiple books. One-to-many relationship
    with the Book model.
    """
    name = models.CharField(max_length=255)

class Book(models.Model):
    """
    Represents a book written by an author. Contains the title, year of publication,
    and a foreign key to the Author model.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
