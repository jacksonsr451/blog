from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin_area/', admin.site.urls),
    path('' , views.home, name='home'),
    path('admin/', include('admin_area.urls')),
]
