# documentscanner/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from scanner import views  # Import the views from your app

urlpatterns = [
    path('', views.upload_document, name='upload_document'),
    # Add other URL patterns here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # This line serves media files during development
