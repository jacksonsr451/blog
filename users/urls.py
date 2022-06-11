from django.urls import path
from .views import editors

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
]
