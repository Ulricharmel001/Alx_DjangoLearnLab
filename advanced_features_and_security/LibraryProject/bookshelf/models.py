from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser, UserManager
from django.contrib.auth.models import Group, Permission, User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField( auto_now=False, auto_now_add=False, default='2000-01-01')

    def __str__(self):
        return f"{self.title} by: {self.author} published in: {self.publication_year}"
 
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]


# Creating custom User model
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password,  **extra_fields):
        if not email:
            raise ValueError('User must have email')
        user= self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # Add this line to fix the missing username error
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(unique=False, max_length=200)
    date_of_birth = models.DateField(null=True, blank=True, default='2000-01-01')
    profile_photo = models.ImageField(upload_to='profile_photo/', height_field=None, width_field=None, max_length=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Add 'username' here to make it required for createsuperuser
    objects = CustomUserManager()