from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)  # Optional title field
    file = models.FileField(upload_to='documents/')  # The actual file upload field
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp when uploaded


    def __str__(self):
        return self.title


# Create your models here.
