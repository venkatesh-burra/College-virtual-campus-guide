"""
Main URL configuration for QIS Virtual Campus Guide.
Routes requests to each app's urls.py file.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),
    path('enquiry/', include('enquiry.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin panel
import qis_campus.admin_config  # noqa: F401, E402
