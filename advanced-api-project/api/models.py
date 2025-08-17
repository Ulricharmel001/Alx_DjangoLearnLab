from django.db import models

# Create your models here.
from django.db import models

# Author model represents a writer who can have many books.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores author name

    def __str__(self):
        return self.name


# Book model represents a single book written by an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(
        Author,
        related_name='books',  # allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
