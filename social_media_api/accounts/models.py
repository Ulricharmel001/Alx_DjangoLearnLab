from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

def user_profile_upload_path(instance, filename):
    return f'profiles/user_{instance.id}/{filename}'

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    def __str__(self):
        return self.username
    