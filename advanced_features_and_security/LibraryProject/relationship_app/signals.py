from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, CustomUser  # Use your custom user model, not built-in User

# This function listens for the post_save signal on the CustomUser model
# It runs when a new CustomUser instance is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Automatically create a UserProfile for the new user
        UserProfile.objects.create(user=instance, role=instance.role)



