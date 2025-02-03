# scanner/urls.py
from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.upload_document, name='upload_document'),  # Add this line for the upload route
]
