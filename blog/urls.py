from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin_area/', admin.site.urls),
    path('' , views.home, name='home'),
    path('admin/', include('admin_area.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
