from django import forms
from .models import Document  # Assuming you have a Document model

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')  # Fields you want in the form

    # Validate the file type
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise forms.ValidationError("No file selected.")
        
        # Allow only PDF and image files
        if not (file.name.endswith('.pdf') or file.name.endswith(('.jpg', '.jpeg', '.png'))):
            raise forms.ValidationError("File must be a PDF or an image (jpg, jpeg, png).")
        
        return file
