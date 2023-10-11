from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from user.models import CustomUser
from .models import UserProfile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        user_profile = UserProfile.objects.create( # noqa
            user=user,
            name=user.first_name
        )


@receiver(post_save, sender=UserProfile)
def update_profile(sender, created, instance, **kwargs):
    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.name
        user.email = profile.user.email
        user.save()


@receiver(post_delete, sender=UserProfile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
