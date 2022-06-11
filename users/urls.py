from django.urls import path
from .views import editors, users

urlpatterns = [
    path('editors/', editors.home_editor, name='home_editor'),
    path('editors/add/', editors.add_editor, name='add_editor'),
    path('editors/insert/', editors.insert_editor, name='insert_editor'),
    path('editors/list/', editors.list_editor, name='list_editor'),
    path('editors/change/', editors.change_editor, name='change_editor'),
    path('editors/delete/', editors.delete_editor, name='delete_editor'),
    path('editors/invite/', editors.invite_editor, name='invite_editor'),
    path('editors/update/', editors.update_editor, name='update_editor'),
    path('editors/ban/', editors.ban_editor, name='ban_editor'),
    
    path('users/', users.home_user, name='home_user'),
    path('users/add/', users.add_user, name='add_user'),
    path('users/insert/', users.insert_user, name='insert_user'),
    path('users/list/', users.list_user, name='list_user'),
    path('users/change/', users.change_user, name='change_user'),
    path('users/delete/', users.delete_user, name='delete_user'),
    path('users/invite/', users.invite_user, name='invite_user'),
    path('users/update/', users.update_user, name='update_user'),
    path('users/ban/', users.ban_user, name='ban_user'),
]
