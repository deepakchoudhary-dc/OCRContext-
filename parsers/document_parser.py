# Supported extensions
SUPPORTED_EXTENSIONS = ['.pdf', '.docx', '.png', '.jpg', '.jpeg']

import os
from typing import List

def parse_document(file_path: str) -> str:
    """
    Parse a document (PDF, DOCX, or image) and return extracted text.
    Uses OCR for images and PDF fallback.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return _parse_pdf(file_path)
    elif ext == '.docx':
        return _parse_docx(file_path)
    elif ext in ['.png', '.jpg', '.jpeg']:
        return _parse_image(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def _parse_pdf(file_path: str) -> str:
    try:
        from pdfplumber import open as pdfplumber_open
        text = ""
        with pdfplumber_open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        if text.strip():
            return text
    except Exception:
        pass
    # Fallback to OCR if text extraction fails
    from pdf2image import convert_from_path
    return _ocr_images(convert_from_path(file_path))

def _parse_docx(file_path: str) -> str:
    from docx import Document
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def _parse_image(file_path: str) -> str:
    from PIL import Image
    img = Image.open(file_path)
    return _ocr_images([img])

def _ocr_images(images: List[object]) -> str:
    import pytesseract
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img) + '\n'
    return text.strip()
 