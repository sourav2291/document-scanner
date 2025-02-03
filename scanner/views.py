from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from django.shortcuts import render
from .forms import DocumentForm
from .models import Document

# Tesseract path (update as needed)
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'

def upload_document(request):
    extracted_text = ""
    error_message = ""

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                document = form.save()  # Save uploaded file
                file_path = document.file.path

                if file_path.endswith('.pdf'):
                    # Convert PDF to images
                    images = convert_from_path(file_path)
                    for page_number, image in enumerate(images):
                        extracted_text += f"\n\n--- Page {page_number + 1} ---\n\n"
                        extracted_text += pytesseract.image_to_string(image)
                else:
                    # Open and process the image
                    image = Image.open(file_path)
                    extracted_text = pytesseract.image_to_string(image)
                    
                # If no text is extracted, provide a message
                if not extracted_text.strip():
                    extracted_text = "No text could be extracted from this file."
                
            except Exception as e:
                error_message = f"An error occurred: {e}"
        else:
            error_message = "Invalid file format. Please upload an image or PDF."

    else:
        form = DocumentForm()

    return render(request, 'scanner/upload.html', {
        'form': form,
        'extracted_text': extracted_text,
        'error_message': error_message,
    })
