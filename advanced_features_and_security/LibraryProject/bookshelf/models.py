from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser, UserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by: {self.author} published in: {self.publication_year}"
    


# Creating custom User model
class BaseUserManager(BaseExceptionGroup):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have email')
        user= self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def Create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(unique=False, max_length=200)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField( upload_to='profile_photo/', height_field=None, width_field=None, max_length=None)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []
    objects= UserManager