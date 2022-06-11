from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role, clear_roles


@receiver(post_save, sender=Users)
def assign_user_role(sender, instance, created, **kwargs):
    # TODO: Use the created flag to check if the user is new or not
    if created:
        if instance.occupation == 'editor':
            assign_role(instance, 'editor')
        elif instance.occupation == 'admin':
            assign_role(instance, 'admin')
        elif instance.occupation == 'user':
            assign_role(instance, 'user')
    elif not created:
        if instance.occupation == 'guest':
            clear_roles(instance)
            assign_role(instance, 'guest')
        elif instance.occupation == 'banned':
            clear_roles(instance)
            assign_role(instance, 'banned')
        elif instance.occupation == 'editor':
            clear_roles(instance)
            assign_role(instance, 'editor')
        elif instance.occupation == 'admin':
            clear_roles(instance)
            assign_role(instance, 'admin')
        elif instance.occupation == 'user':
            clear_roles(instance)
            assign_role(instance, 'user')
