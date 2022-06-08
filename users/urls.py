from django.urls import path
from . import views

urlpatterns = [
    path('add_editor/', views.add_editor, name='add_editor'),
    path('insert_editor/', views.insert_editor, name='insert_editor'),
]
