from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choice_occupation = (
        ('admin', 'Administrador'),
        ('user', 'Usuario'),
        ('editor', 'Editor'),
        ('guest', 'Invitado'),
        ('banned', 'Banido'),
        ('deleted', 'Eliminado'),
    )
    occupation = models.CharField(max_length=100, choices=choice_occupation, default='user')
