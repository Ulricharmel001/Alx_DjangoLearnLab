from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

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


    def __str__(self):
        return f"{self.user.username} - {self.role}"




class CustomUserManager(BaseUserManager):
 

    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an emailS')
        user= self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password ):
       user = self.create_user
       user.is_staff = True
       user.is_superuser = True
       user.save(using=self._db)
       return user
       
        


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=CustomUser.ROLE_CHOICES)  