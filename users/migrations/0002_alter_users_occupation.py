# Generated by Django 4.0.5 on 2022-06-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='occupation',
            field=models.CharField(choices=[('admin', 'Administrador'), ('user', 'Usuario'), ('editor', 'Editor'), ('guest', 'Invitado'), ('banned', 'Banido'), ('deleted', 'Eliminado')], default='user', max_length=100),
        ),
    ]