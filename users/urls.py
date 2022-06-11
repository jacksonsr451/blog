from django.urls import path
from . import views

urlpatterns = [
    path('editors/', views.home_editor, name='home_editor'),
    path('editors/add/', views.add_editor, name='add_editor'),
    path('editors/insert/', views.insert_editor, name='insert_editor'),
    path('editors/list/', views.list_editor, name='list_editor'),
    path('editors/change/', views.change_editor, name='change_editor'),
    path('editors/delete/', views.delete_editor, name='delete_editor'),
    path('editors/invite/', views.invite_editor, name='invite_editor'),
    path('editors/update/', views.update_editor, name='update_editor'),
    path('editors/ban/', views.ban_editor, name='ban_editor'),
]
