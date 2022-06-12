from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.admin_area, name='admin_area'),
    path('users/', include('users.urls')),
]
