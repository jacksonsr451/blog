from django.urls import path
from . import views

urlpatterns = [
    path('editor/', views.home_editor, name='home_editor'),
    path('add_editor/', views.add_editor, name='add_editor'),
    path('insert_editor/', views.insert_editor, name='insert_editor'),
    path('list_editor/', views.list_editor, name='list_editor'),
    path('change_editor/', views.change_editor, name='change_editor'),
    path('delete_editor/', views.delete_editor, name='delete_editor'),
    path('invite_editor/', views.invite_editor, name='invite_editor'),
    path('update_editor/', views.update_editor, name='update_editor'),
    path('ban_editor/', views.ban_editor, name='ban_editor'),
]
