from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role


@receiver(post_save, sender=Users)
def assign_user_role(sender, instance, created, **kwargs):
    if created:
        if instance.occupation == 'editor':
            assign_role(instance, 'editor')
        elif instance.occupation == 'admin':
            assign_role(instance, 'admin')
        elif instance.occupation == 'user':
            assign_role(instance, 'user')
        elif instance.occupation == 'guest':
            assign_role(instance, 'guest')
        elif instance.occupation == 'banned':
            assign_role(instance, 'banned')
        elif instance.occupation == 'deleted':
            assign_role(instance, 'deleted')
