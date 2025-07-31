from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# ========================
# Author Model
# ========================
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# ========================
# Book Model
# ========================
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

# ========================
# Library Model
# ========================
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return f"Library: {self.name} ({self.books.count()} books)"

# ========================
# Librarian Model
# ========================
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian: {self.name}, Library: {self.library.name}"

# ========================
# Custom User Model
# ========================
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return self.username

# ========================
# User Profile Model
# ========================
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=CustomUser.ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
