from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role, clear_roles


@receiver(post_save, sender=Users)
def assign_user_role(sender, instance, created, **kwargs):
    if_created_instance(sender, instance, created, **kwargs)
    if_update_instance(sender, instance, created, **kwargs)

def if_created_instance(sender, instance, created, **kwargs):
    if created:
        create_role_instance(instance, 'editor', 'editor')
        create_role_instance(instance, 'admin', 'admin')
        create_role_instance(instance, 'user', 'user')

def if_update_instance(sender, instance, created, **kwargs):
    if not created:
        update_role_instance(instance, 'guest', 'guest')
        update_role_instance(instance, 'banned', 'banned')
        update_role_instance(instance, 'editor', 'editor')
        update_role_instance(instance, 'admin', 'admin')
        update_role_instance(instance, 'user', 'user')

def create_role_instance(instance, role, method):
    if instance.occupation == role:
        assign_role(instance, method)

def update_role_instance(instance, role, method):
    if instance.occupation == role:
        clear_roles(instance)
        assign_role(instance, method)
